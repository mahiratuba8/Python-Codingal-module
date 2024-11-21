#take two inputs from the user for the height and weight. then calculate bmi using formula, bmi=weight/(height/100)**2
#if bmi is less then equal to 18.4, then you are under weight
#if bmi is less then equal to 24.9, then you are healthy
#if bmi is less then equal to 29.9, then you are over weight
#if bmi is less then equal to 34.9, then you are severlly overweight
#if bmi is less then equal to 39.9, then you are ur obese
#else you ae seveally obease

weight=(float(input("Write you weight")))
height=(float(input("Enter your height")))
bmi=(weight/(height/100)**2)
if (bmi<=18.4):
    print("You are under weight.")
elif (bmi<=24.9):
    print("You are healthy.")
elif (bmi<=29.9):
    print("You are over weight.")
elif(bmi<=34.9):
    print("You are severally over weight.")

elif (bmi<=39.9):
    print("Your are obese")
else:
    print("You are severally obese.")

