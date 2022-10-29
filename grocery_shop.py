print("welcome to grocery shop")
quantity = int(input("enter your quantity : "))
price = int(input("enter your price : "))

total_price = quantity * price
dis_amt = total_price * 0.1
final_amt_pay = 0 

if total_price > 1000:
    final_amt_pay = total_price - dis_amt 
    print(f"your final bill is : {final_amt_pay}")

else :
    print(f"your final bill is : {total_price}")