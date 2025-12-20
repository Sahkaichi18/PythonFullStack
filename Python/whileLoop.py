a = int(input("Enter the start number to start the table : "))
b = int(input("Enter the end number for ending the table : "))

while(a <= b):                                                                                                    
    c = 1
    while (c <= 10):
        result = a * c
        print(a, "X", c, "=", result )
        c += 1

    #f string ex : (f"{}")