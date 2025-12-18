

c = (int(input("Enter the marks for C : ")))
java = (int(input("Enter the marks for Java : ")))
python = (int(input("Enter the marks for Python : ")))
dsa = (int(input("Enter the marks for DSA : ")))
oops = (int(input("Enter the marks for OOPS : ")))

total = c+java+python+dsa+oops
print("Your total marks is : ", total)

if (total >= 500):
    print(total , "You have got invalid marks !")

percentage = total/500 * 100
print("Your percentage is : ", percentage)

if(c>=100 or java>= 100 or python >= 100 or dsa >= 100 or oops >= 100):
    print("Invalid marks entered")

if(percentage > 100):
    print(percentage, "%","It is an Invalid percentage !")
elif(percentage >= 90):
    print("You achieved A grade with", percentage ,"%")
elif(percentage >= 75):
    print("You achieved B grade with", percentage ,"%")
elif(percentage >= 60):
    print("You achieved C grade with", percentage ,"%")
elif(percentage >= 35):
    print("You achieved D grade with", percentage ,"%")
else :
    print("You have F grade with", percentage ,"%")










