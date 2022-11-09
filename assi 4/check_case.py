a=input("Enter any string: ")
j = -1 
flag = 0 
for i in a:
    if(i != a[j]):
        flag = 1
        break
    j = j-1 

if flag == 1 :
    print("String entered is not a palindrome")
else:
    print("String entered is a palindrome")