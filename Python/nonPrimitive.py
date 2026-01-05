data = {
    1: ["Sahil", "Hritik", "Rahul", "Rakesh"],
    2: [515, 153, 152, 554],
    3: [2009, 2014, 1153, 1317]
}

#Count of vowels and consonants

vowel = 0
consonant = 0

for name in data[1]:
    for ch in name:
        if ch in "aeiouAEIOU":
            vowel += 1
        else:
            consonant += 1
print("Count of vowel is :", vowel)
print("Count of consonant is :", consonant)

print("---------------------")

#Sum of numbers

for number in data[2]:
        temp = number
        sum = 0

        while temp > 0:
            digit = temp % 10
            sum += digit
            temp //= 10

        print("Sum of digits of", number, "is", sum)

print("------------------")

for year in data[3]:
     if(year % 4 == 0):
        print(year, "is a leap year")
     elif(year % 100 == 0):
        print(year , "is not a leap year")
     elif(year % 400 == 0):
        print(year, "is a leap year")
     else:
        print(year, "is not a leap year")




