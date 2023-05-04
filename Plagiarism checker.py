from difflib import SequenceMatcher

First_String = input("Enter the First String: ")
Second_String = input("Enter the Second String: ")

match = SequenceMatcher(None, First_String, Second_String)

Plagiarised_Percent= match.ratio() * 100

print("The Plagiarised percent in given strings are: ", int(Plagiarised_Percent), "%")
