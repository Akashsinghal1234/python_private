print("to find the year is leap or not ")

year = int(input("enter the year you want to check : "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) :
    print(f"year {year} is a leap year")
else: 
    print("its not a leap year")

