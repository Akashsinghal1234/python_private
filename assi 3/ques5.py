mod = 0 
final = 0 
for i in range (100, 500):
    final = 0
    temp = i
    while (i > 0):
        mod = i % 10
        i = i // 10
        final = final + mod**3

    if final == temp :
       print(temp)








