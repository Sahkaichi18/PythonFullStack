a = 1,2,3,4,5
print(type(a))
#default is tuyple if writne like a = 1,2,3,4,

#item assignment not allowed means changing values not allowed 
# a[1]=30

a = 1,2,3,4,5
sum = 0
#to show addition of the 1st and 2nd number.

for i in range(0,len(a)):
    sum += a[i]
    print(sum)
# for i in a:
#     sum += i
#     print(sum)

