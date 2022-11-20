a = input("enter").split()
d4 = {}
for i in a :
    if i in d4.keys() :
        d4[i] += 1 
    else:
        d4[i] = 1
print(d4)