age = int(input("Enter your age:"))
gra = int(input("Enter your grade:"))

if age < 14:
    print("You are not eligible for the exam.")

elif age >= 14:
    print("Valid")

elif age == " ":
    print("Enter number")

else:
    print("Invalid")

if gra< 8:
    print("You are not eligible for the exam")

elif gra > 8:
    print("Your are eligible for the exam")

else:
    print("Invalid")




