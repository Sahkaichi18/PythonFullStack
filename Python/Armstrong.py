# user input a number of 3 digit.....check if its an armstrong.

num = int(input("Enter a 3 digit number : "))

if num >= 100 and num <= 999:

    og = num
    sum = 0

    while num > 0:
        digit = num % 10
        sum += digit * digit * digit   # digit ** 3  (We can use it as well in python)
        num //= 10

    if sum == og:
        print(og, "is an Armstrong number")
    else:
        print(og, "is not an Armstrong number")
else:
    print(num ,"is not a 3 digit number")
