number = int(input("enter the number to reverse : "))
#123
rev = 0 
m = 0
while (number > 0):
    m = number % 10 #save the last number of input
    number = int (number / 10)
    rev = rev * 10 + m
print(rev)
