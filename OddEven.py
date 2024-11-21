num=int(input("enter a number "))
if num<=50:
    print(f"{num} is less then equal to 50") 
    if num % 2==0:
       print(f"{num} is and even number. ")
    else:
       print(f"{num} is odd number.")
else:
    print("number is greater then 50")

