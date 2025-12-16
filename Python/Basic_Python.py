# print("hello world")

a =10
print(a)
print(a+5)

b = "name"
print(type(b))

#Operators 

#Arithmetic Operators

x = 10
y = 4
print(x+y)
print(x-y)
print(x*y)
print(x/y)          

#Assignment Operators

a = 5
b = 10

a += b  # a = a + b
print(a)

a -=b
print(a) #a = a - b

a *= b
print(a) # a = a * b        

a /= b
print(a) # a = a / b

a %= b
print(a) # a = a % b

#comparison operator 

p = 30
q = 40

print(p == q)  # equal to
print(p != q)  # not equal to 
print(p > q)   # greater than
print(p < q)   # less than
print(p >= q)  # greater than or equal to
print(p <= q)  # less than or equal to

#logical operators 

m = True
n = False

print(m and n)  # logical AND
print(m or n)   # logical OR        
print(not m)    # logical NOT
print(not n)    # logical NOT
print(m and not n)  # logical AND with NOT

#decision making
#1.conditional statements
#2 control statemtents

#if elif else example

a = 10
b = 20
c = 15 

if a >b and  a >c:
    print("a is the largest")
elif b > a and b > c:
    print("b is the largest")
else:
    print("c is the largest")
    
