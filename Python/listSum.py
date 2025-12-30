# a = [1539, 5579, 5545, 3173]

# sum = 0
# # for i in range(len(a)):
# #         sum = sum + a[i]
# #         print(sum)

# for Bnum in a:
#     for Snum in Bnum:
#         sum = sum + a[Snum]

#         while Bnum > 0:
#             digit = Bnum % 10
#             sum += a[Snum]
#             num //= 10

#             print(sum)


a = [1539, 5579, 5545, 3173]

for Bnum in a:
        temp = Bnum
        sum = 0

        while temp > 0:
            digit = temp % 10
            sum += digit
            temp //= 10

        print("Sum of digits of", Bnum, "is", sum)
