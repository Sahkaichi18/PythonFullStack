a = [2014, 2003, 2004, 2028, 2024, 2025]

for year in a:
    if(year % 4 == 0):
        print(year, "is a leap year")
    elif(year % 100 == 0):
        print(year , "is not a leap year")
    elif(year % 400 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")

   
