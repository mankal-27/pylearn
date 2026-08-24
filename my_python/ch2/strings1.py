#Math
password = "123a"
print(len(password))

if(len(password) < 8):
    print("Ur Password is too short")
else:
    print("Password accepted")


text = """
Python is easy to learn.
Python is powerful.
Many people love Python.
"""

text_count = text.count("Python")
print(text_count)

#Transformation
date = "2026/05/10"
date_replaced = date.replace("/", "-")
print(date_replaced)

phone = "99-893-999-12"
print(phone.replace("-", ""))

price = "$12,99.99"
print(price.replace("$", "").replace(",", ""))

phine = "+41 (176) 123-4567"
print(phine.replace(" ", "").replace("+", "00").replace("-", "").replace("(", "").replace(")", ""))

name = 'Manju'
age = 35
is_student = False

print(f"My name is {name} and my Age is {age} and my student status is {is_student} {{and i love it here}}")

stamp = "2026-08-22 14:30"
print(stamp.split(" "))

stamp_date = "2026-08-22"
print(stamp_date.split("-"))

stringRepeat = "ha" * 3
print(stringRepeat)

#Indexing And Slicing

string1 = "hellomydatling"
print(string1[0])
#Extraction

string1Splice = string1[0:3]
print(string1Splice)
print(string1[0:-1:2])

#Clearn Whitespace
cleanWhiteSpace1 = "           Hello world"
cleanWhiteSpace2 = "Hello World         "
print(cleanWhiteSpace1.lstrip())
print(cleanWhiteSpace2.rstrip())
print(cleanWhiteSpace1.strip())
print(cleanWhiteSpace2.strip())

cleanWhiteSpace3 = "######ABBC######"
#print(cleanWhiteSpace3.strip("#"))

print(len(cleanWhiteSpace3))
print(len(cleanWhiteSpace3.strip("#")))

nr_of_spaces = len(cleanWhiteSpace3) - len(cleanWhiteSpace3.strip("#"))
isClean = len(cleanWhiteSpace3) == len(cleanWhiteSpace3.strip("#"))
print("Nr of Spaces: ", nr_of_spaces)
print("Is my data Clean ? ", isClean)

#case Conversions

text1 = "python Programming"
print(text1.lower())
print(text1.upper())

search = "Email "
data = "  emAil"

print(search == data)
print(search.lower().strip() == data.lower().strip())

text2 = "968-Maria, ( D@t@ Engineer ) ;; 27y  "

final = text2.replace("968", "name").replace("-", ": ").replace("@","a").replace("( ", "| role: ").replace(")", "|").replace(";;", " age: ").replace("y", "").replace(",", "").strip()

print(final.lower())

#Search

search1 = "2025-Feb-10"
print(search1.startswith("2025"))
print(search1.endswith("00"))
print(search1.find("Feb"))
print("be" in search1)

#Validation
country = "USA"
print(country.isalpha())

phine1 = "997376366"
print(phine1.isnumeric())