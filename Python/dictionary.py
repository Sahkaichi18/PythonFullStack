#set data cant change values and cant add duplicates
#Sets are unordered in Python

# a = {30,20,10,40,100}
# print(a)

# DICTIONARY
# can store duplicate values but not keys

# a = {1:10, 3:20, 9:100}
# sum = 0
# for i in a:
#     sum+=a[i]
#     print(sum)

#Reverse name in dictionary

s = {1:'Sahil', 2:'Hritik', 3:'Rudra'}

for key in s:
    name = s[key]
    rev = ""
    for ch in name:
        rev = ch + rev
    print(rev)


