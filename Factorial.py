def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)
num = int(input("Enter your value:"))
if num < 0:
    print("Sorry, factorial value does not exist for negative numbers!")
elif num == 0:
    print("The factorial value of 0 is 1.")
else:
    print("The factorial value of your number is:",num,"is",recur_factorial(num))
