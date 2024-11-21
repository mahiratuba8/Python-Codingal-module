def intro(parameters):
    print("My name is", parameters)
firstname=input("enter your first name")
intro(firstname)

def about(information):
    print("Codingal is a platform for education.", information)
name= input("What do you want to know about? ")
about(name)

def recursion(x):
    if x==1:
        return x
    else: 
        return x*recursion(x-1)
    
number=int(input("Enter the number: "))
if number<0:
    print("factoral doesn't exist for negative, positive only.")
elif number==0:
    print("the factoral of 0 is 1")

else:
    print("the factorial of", number, "is", recursion(number))