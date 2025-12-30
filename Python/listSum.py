a = [1539, 5579, 5545, 3173]

sum = 0
# for i in range(len(a)):
#         sum = sum + a[i]
#         print(sum)

for Bnum in a:
        while Bnum > 0:
            for Snum in Bnum:
                digit = Bnum % 10
                sum += a[Snum]
                num //= 10

                print(sum)