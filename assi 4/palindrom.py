string_to_check = input("enter your word : ") 
empty_string = ""
for i in string_to_check:
    empty_string = i + empty_string
 
if (string_to_check == empty_string):
    print("Yes")
else:
    print("No")