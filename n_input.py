from enum import Flag


n = int(input("enter your number : "))
flag = False
if n > 0 :
    flag = True
    print(n*n)
    print(flag)
elif n < 0 : 
    flag = True
    print(n*n*n)
    print(flag)
else :
    print("input was zero")
    
