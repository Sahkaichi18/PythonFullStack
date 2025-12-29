#check the palindrome of the given list


a = ["data", "science", "python", "java", "html", "madam"]

for word in a:
    rev = ""
    for char in word:
        rev = char + rev

    print("Word:", word)
    print("Reverse:", rev)

    if word == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")

    print()

