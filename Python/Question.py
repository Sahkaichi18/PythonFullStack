# user input a number of 3 digit.....check if its an armstrong.
# Make a hotel management having 5 products.....user selects it and let there be a choice of payment

# num = (int(input("Enter a 3 digit number : ")))
# if (num*num*num +num == num):
#     print(num ,"is an armstrong")
# else:
#     print(num ,"is not an armstrong")

num = int(input("Enter a 3-digit number: "))

if num >=100 and num <=999:

    original = num
    sum_of_cubes = 0

    while num > 0:
        digit = num % 10
        sum_of_cubes += digit * digit * digit   # instead of **
        num //= 10

    if sum_of_cubes == original:
        print(original, "is an Armstrong number")
    else:
        print(original, "is not an Armstrong number")

        print(original, "is not an Armstrong number")
else:
    print(num ,"is not a 3 digit number")