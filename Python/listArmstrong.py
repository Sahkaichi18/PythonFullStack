#Get the armstrong of the given list

b = [159, 133, 393, 904, 204]

for num in b:
    sum = 0
    og = num
    if num > 0:
        digit = num % 10
        sum += digit * digit * digit
        num //= 10

        if sum == og:
            print(og, "is an Armstrong number")
    else:
        print(og, "is not an Armstrong number")
else:
    print(num ,"is not a 3 digit number")
