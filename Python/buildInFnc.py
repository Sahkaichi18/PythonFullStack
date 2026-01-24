print("Case conversion")

s = 'hello world'
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())

print("--------------------------------")

print("Search and replace")

text = "Python is fun, and python is powerful."
print(text.index('Python'))
print(text.replace("Python", "Java"))
print(text.count("n"))

print("--------------------------------")

print("Formatting")

word = "Python"
print(word.strip())
print(word.lstrip())
print(word.rstrip())
print(word.center(100, '-'))
print(word.ljust(100, '*'))
print(word.rjust(100, '*'))

print("--------------------------------")

print("Validation")

print("Python123".isalnum())
print("Hello".isalpha())
print(" ".isspace())
print("python".islower())
print("PYTHON".isupper())

print("--------------------------------")

print("Splitting and joining")

data = "apple,banana,grape"
print(data.split(","))
print(data.rsplit(",", 1))

text2 = "Hello \nWorld"
print(text2.splitlines())

words = ['i', 'love', 'python']
print("".join(words))

print("--------------------------------")

print("String Checking")

print("HelloWorld".startswith("Hello"))
print("HellowWorld".endswith("World"))

print("--------------------------------")

print("Others")

print(len("Python"))

print(ord('A'))   # ASCII values: 48–57 → 0–9, 65–90 → A–Z, 97–122 → a–z
print(chr(65))

print("My name is {0} and i am {1} years old{2}".format("Alice", 25, "."))

print("--------------------------------")

s = input("Enter string: ")

if len(s) > 1:
    result = s[0].upper() + s[1:-1] + s[-1].upper()
else:
    result = s.upper()

print(result)

print("--------------------------------")

s2 = "hello world"
print(s2.split()[0].upper())

print("Helloworld".startswith("Hello"))

print("--------------------------------")

print(len("Python"))
