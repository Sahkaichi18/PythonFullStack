# make the reverse of the string

a = ["data", "science", "python", "java", "html"]

for i in a:
    rev = ""          
    for j in i:
        rev = j + rev
    print(rev)
