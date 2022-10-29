print("welcome to insurence company")

status = input("married or unmarried ")

if status == "married":
    print("you are insured")
elif status == "unmarried":
    sex = input("male or female")
    age = int(input("enter your current age : "))
    if sex == "male" and age > 30 :
        print("you are insured, good to go")
    elif sex =="female" and age > 25 :
        print("you are insured, good to go see you")
    else:
        print("you are not insured")
else:
    print("invalid input")
    