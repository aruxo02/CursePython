# Simple Text Analyzer

text = input("Enter some text to analyze: ")
print("Need 3 letters:")
a = input("Enter the first letter: ")
b = input("Enter the second letter: ")
c = input("Enter the third letter: ")

print("\nThe analysis of the text is as follows:")
print(f"The letter {a} appears {text.lower().count(str(a).lower())}")
print(f"The letter {b} appears {text.lower().count(str(b).lower())}")
print(f"The letter {c} appears {text.lower().count(str(c).lower())}")

print(f"The initial text has {len(text.split())} words")
print(f"The first letter of the text is {text[0]} and the last is {text[-1]}")

print("The order of words in reverse would be:")
word_list = text.split()
word_list.reverse()
reversed_text = " ".join(word_list)
print(reversed_text)

my_bool = "Python" in text
result_map = {True: "Yes", False: "No"}

print(f"{result_map[my_bool]} contains the word python") 





