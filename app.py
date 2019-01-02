print("Hello World")

# prints a new line
print("\n")

print("Printing a triangle below")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

print("\n")

my_first_name = "Vino"
my_last_name = "Dharani"
my_age = 29
is_male = True
print("Hello " + my_first_name + " " + my_last_name)

print("\n")

phrase = "Giraffe Academy"
print("phrase in lower case is -> " + phrase.lower())
print("phrase in upper case is -> " + phrase.upper())
print(phrase.islower())
print(phrase.isupper())
print(phrase.lower().islower())

# length function
print("Length of the phrase is ")
print(len(phrase))

# Characters of the string can be accessed by their index, just like an array
# Index starts with zero
print("First character of the phrase is " + phrase[0])

# index function
print(phrase.index("G"))
print(phrase.index("a"))
print(phrase.index("ira"))
# the below line throws an error
# print(phrase.index("xx"))

print(phrase.replace("Giraffe", "Elephant"))
