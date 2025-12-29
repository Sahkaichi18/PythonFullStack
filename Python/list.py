#list is denoted by square brackets

# every value in square brackets has index

# we can update the elements in list

# a = [1,2,3,4,5,6,7,8]
# print(a)
# print("-------------------------")
# a[4]= 33
# print(a)
# print("-------------------------")
# print (a[1:4])

# for i in range(0, len(a)):
#     print(a[i])

# for i in a:
#     print(a)

b = [10, 20, 30, 40, 50, 98, 17, 11, 2]

# sum = 0
# for i in range(len(b)):
#     sum = sum + b[i]
#     print(sum)

for i in b:
#     sum+=i
# print("The sum is", sum)

    if i%2==0:
        print(i," is an even number")
    else:
        print(i, " is an odd number")



