'''
. Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’.
'''
try:
    with open("poems.txt", "r") as f:  # Using 'with open' ensures file closure
        text = f.read().lower()  # Convert text to lowercase for case-insensitive search

    if "twinkle" in text:
        print("Twinkle is present in the text")
    else:
        print("Twinkle is not present in the text")

except FileNotFoundError:
    print("Error: 'poems.txt' file not found!")
except Exception as e:
    print(f"An error occurred: {e}")
