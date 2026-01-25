# print("Case conversion")

# s = 'hello world'
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.capitalize())

# print("--------------------------------")

# print("Search and replace")

# text = "Python is fun, and python is powerful."
# print(text.index('Python'))
# print(text.replace("Python", "Java"))
# print(text.count("n"))

# print("--------------------------------")

# print("Formatting")

# word = "  Python      programing  "
# print(word.strip()) #Removes spaces from BOTH left and right sides
# print(word.lstrip()) #Removes spaces from LEFT side only
# print(word.rstrip()) #Removes spaces from RIGHT side only
# print(word.center(100, '-')) #Places the word in the center of a string of length 100 and Fills remaining spaces with -
# print(word.ljust(100, '*')) #Left-aligns the word and Fills remaining right side with * until length is 100
# print(word.rjust(100, '*')) #Right-aligns the word and Fills remaining left side with * until length is 100

# print("--------------------------------")

# print("Validation")

# #Returns True if the string contains ONLY alphabets (A–Z, a–z) and digits (0–9) and No spaces, no symbols allowed
# #Returns True if the string contains ONLY alphabets, if Digits, spaces, symbols then False
# #Returns True if the string contains ONLY whitespace
# #Returns True if all alphabetic characters are lowercase
# #Returns True if all alphabetic characters are uppercase
# #Returns true if the string conatians number only.

# print("--------------------------------")

# print("Splitting and joining")

# data = "apple,banana,grape"
# print(data.split(",")) #Splits a string into a list using the given separator. Here, the separator is ,
# print(data.rsplit(",",1)) #Splits the string from the right side. 1 means only one split

# text2 = "Hello \nWorld"
# print(text2.splitlines()) #Splits the string at line breaks

# words = ['i', 'love', 'python']
# print("".join(words))

# print("--------------------------------")

# print("String Checking")
print("HelloWorld".startswith("Hello")) #Checks whether the string begins with the given value
print("HellowWorld".endswith("World")) #Checks whether the string ends with the given value

# print("--------------------------------")

# print("Others")

# print(len("Python"))

# print(ord('A'))   # ASCII values: 48–57 → 0–9, 65–90 → A–Z, 97–122 → a–z
# print(chr(65))

# print("My name is {0} and i am {1} years old{2}".format("Alice", 25, "."))

# print("--------------------------------")

# s = input("Enter string: ")

# if len(s) > 1:
#     result = s[0].upper() + s[1:-1] + s[-1].upper()
# else:
#     result = s.upper()

# print(result)

# print("--------------------------------")

# s2 = "hello world"
# print(s2.split()[0].upper())

# print("Helloworld".startswith("Hello"))

# print("--------------------------------")

# print(len("Python"))
