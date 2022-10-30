salary = int(input("ener your base salary : "))
a = 0
if salary < 1500 :
    hra = salary * 0.1
    da = salary * 0.9
    a = salary + hra + da 
    print(a)

else : 
    hra = 500 
    da = salary * 0.98 
    a = salary + hra + da 
    print(a)


    
