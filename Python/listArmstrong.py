#Get the armstrong of the given list

# b = [153, 133, 393, 904, 204]

# for num in b:
#     sum = 0
#     og = num
#     while num > 0:
#         digit = num % 10
#         sum += digit * digit * digit
#         num //= 10

#         if sum == og:
#             print(og, "is an Armstrong number")
#     else:
#         print(og, "is not an Armstrong number")


b = [153, 133, 393, 904, 204]

for num in b:
    sum = 0
    og = num

    if num >= 100 and num <= 999:
        while num > 0:
            digit = num % 10
            sum += digit * digit * digit
            num //= 10

        if sum == og:
            print(og, "is an Armstrong number")
        else:
            print(og, "is not an Armstrong number")
    else:
        print(og, "is not a 3-digit number")

# multiple years in a list...check if it is a leap year or not 