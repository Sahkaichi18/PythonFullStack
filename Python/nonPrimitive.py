data = {
    1: ["Sahil", "Hritik", "Rahul", "Rakesh"],
    2: [515, 153, 152, 554],
    3: [2009, 2014, 1153, 1317]
}

for name in data[1]:  
    rev = ""
    for ch in name:
        rev = ch + rev
    print(rev)
