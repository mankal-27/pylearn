#!/usr/bin/env python3
"""
Search a folder of PDF files (like the SIR discrepancy reports) for elector
names matching given prefixes (default: kama*, loke*).

Usage:
    python search_names.py /path/to/pdf_folder
    python search_names.py /path/to/pdf_folder --prefixes kama loke ram
    python search_names.py /path/to/pdf_folder --all        # don't stop at first match, scan everything
    python search_names.py file1.pdf file2.pdf ...           # or pass individual files

Requires: pdfplumber  (pip install pdfplumber --break-system-packages)
"""

import argparse
import csv
import os
import re
import sys

try:
    import pdfplumber
except ImportError:
    sys.exit("Missing dependency. Install it with:\n  pip install pdfplumber --break-system-packages")


def find_pdf_files(paths):
    """Expand a list of files/directories into a sorted list of .pdf file paths."""
    pdf_files = []
    for p in paths:
        if os.path.isdir(p):
            for root, _, files in os.walk(p):
                for f in files:
                    if f.lower().endswith(".pdf"):
                        pdf_files.append(os.path.join(root, f))
        elif os.path.isfile(p) and p.lower().endswith(".pdf"):
            pdf_files.append(p)
    return sorted(pdf_files)


def extract_rows_from_pdf(pdf_path):
    """
    Extract table-like rows from a PDF using pdfplumber.
    Falls back to line-based text parsing if no tables are detected.
    Returns a list of dicts: {page, row_text, s_no, part_serial, epic, name, age, gender, reason}
    """
    rows = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            tables = page.extract_tables()
            if tables:
                for table in tables:
                    for row in table:
                        if not row:
                            continue
                        clean_row = [c.strip() if c else "" for c in row]
                        row_text = " | ".join(clean_row)
                        rows.append({
                            "page": page_num,
                            "row_text": row_text,
                            "raw": clean_row,
                        })
            else:
                # Fallback: plain text, line by line
                text = page.extract_text() or ""
                for line in text.split("\n"):
                    line = line.strip()
                    if line:
                        rows.append({
                            "page": page_num,
                            "row_text": line,
                            "raw": None,
                        })
    return rows


def matches_prefix(text, prefixes):
    """Check if any word in `text` starts with any of the given prefixes (case-insensitive)."""
    if not text:
        return None
    words = re.findall(r"[A-Za-z]+", text)
    for w in words:
        for p in prefixes:
            if w.lower().startswith(p.lower()):
                return w
    return None


def search_pdfs(pdf_files, prefixes, stop_on_first=True):
    all_matches = []
    for pdf_path in pdf_files:
        print(f"Scanning: {pdf_path}")
        try:
            rows = extract_rows_from_pdf(pdf_path)
        except Exception as e:
            print(f"  [!] Could not read {pdf_path}: {e}")
            continue

        for row in rows:
            matched_word = matches_prefix(row["row_text"], prefixes)
            if matched_word:
                match = {
                    "file": pdf_path,
                    "page": row["page"],
                    "matched_word": matched_word,
                    "row_text": row["row_text"],
                }
                all_matches.append(match)
                print("\n" + "=" * 70)
                print(f"MATCH FOUND: '{matched_word}'")
                print(f"File : {pdf_path}")
                print(f"Page : {row['page']}")
                print(f"Row  : {row['row_text']}")
                print("=" * 70 + "\n")

                if stop_on_first:
                    return all_matches
    return all_matches


def write_matches_csv(matches, csv_path):
    """
    Write matches to a clean, tabular CSV with one row per match:
    File Name, S.No, Part Serial Number, EPIC Number, Elector Name, Age, Gender, Reason for Discrepancy

    Handles the case where the "Reason for discrepancy" column wraps onto a
    second line inside the PDF (embedded newline) by collapsing it into a
    single space-joined string.
    """
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "File Name", "S.No", "Part Serial Number", "EPIC Number",
            "Elector Name", "Age", "Gender", "Reason for Discrepancy",
        ])
        for m in matches:
            # Collapse embedded newlines (wrapped reason text) into a single space
            row_text = m["row_text"].replace("\n", " ").replace("\r", " ")
            row_text = re.sub(r"\s+", " ", row_text).strip()
            parts = [p.strip() for p in row_text.split("|")]
            # Pad to at least 6 expected columns: SNo, PartSerial, EPIC, Name, Age, Gender
            while len(parts) < 6:
                parts.append("")
            s_no, part_serial, epic, name, age, gender = parts[:6]
            reason = " | ".join(parts[6:]) if len(parts) > 6 else ""
            writer.writerow([
                os.path.basename(m["file"]), s_no, part_serial, epic,
                name, age, gender, reason,
            ])


def main():
    parser = argparse.ArgumentParser(description="Search PDFs for names matching given prefixes.")
    parser.add_argument("paths", nargs="+", help="PDF files and/or folders containing PDFs")
    parser.add_argument("--prefixes", nargs="+", default=["kama", "loke"],
                         help="Name prefixes to search for (default: kama loke)")
    parser.add_argument("--all", action="store_true",
                         help="Scan all files and collect all matches instead of stopping at the first")
    parser.add_argument("--csv", default="matches.csv",
                         help="Path to output CSV file (default: matches.csv)")
    args = parser.parse_args()

    pdf_files = find_pdf_files(args.paths)
    if not pdf_files:
        sys.exit("No PDF files found in the given path(s).")

    print(f"Found {len(pdf_files)} PDF file(s). Searching for prefixes: {args.prefixes}\n")

    matches = search_pdfs(pdf_files, args.prefixes, stop_on_first=not args.all)

    print("\n" + "-" * 70)
    if matches:
        print(f"Total matches found: {len(matches)}")
        if not args.all:
            print("(Stopped at first match. Use --all to scan every file and collect all matches.)")
        write_matches_csv(matches, args.csv)
        print(f"Results written to: {args.csv}")
    else:
        print("No matches found in any of the scanned PDFs.")


if __name__ == "__main__":
    main()