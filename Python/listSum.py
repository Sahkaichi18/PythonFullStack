a = [1539, 5579, 5545, 3173]

sum = 0
# for i in range(len(a)):
#         sum = sum + a[i]
#         print(sum)

for Bnum in a:
    for Snum in Bnum:
        sum = sum + a[Snum]
        print(sum)

        