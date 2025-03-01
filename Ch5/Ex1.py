'''
Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up!
'''

hindi_to_english = {
    "स्वागत": "hello",
    "नाम": "name",
    "विश्वास": "faith",
    "प्रेम": "love",
    "जीवन": "life",
    "जन्म": "birth",
    "मूर्ति": "death",
    "देव": "god",
    "देवता": "deity",
    "देवी": "devi",
    "देवता": "deity",
}

while True:
    word = input("Enter a Hindi word: ")
    if word in hindi_to_english:
        print(f"The English translation of {word} is {hindi_to_english[word]}")
    else:
        print(f"{word} is not in the dictionary.")

    choice = input("Do you want to look up another word? (yes/no): ")
    if choice.lower() != "yes":
        break

print("Goodbye!")
