number = int(input("enter the number to reverse : "))
sum = 0
m = 0
while (number > 0):
    m = number % 10 
    number = int (number / 10)
    sum = sum + m
print(sum)

    








