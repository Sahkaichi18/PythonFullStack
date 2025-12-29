a = ["data", "science", "python", "java", "html"]

rev = ""
for i in a:
    for j in i:
        rev = j+rev
    print(rev)