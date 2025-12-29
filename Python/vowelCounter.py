a = ["data", "science", "python", "java", "html"]

print(a)

vowel = 0
consonant = 0

for i in a:
    for j in i:
        if j in "aeiouAEIOU":
            vowel += 1
        else:
            consonant += 1

print("Count of vowel is :", vowel)
print("Count of consonant is :", consonant)

