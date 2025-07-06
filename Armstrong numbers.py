num = int(input("Enter a 3 digit number:"))
str_num = str(num)

if int(str_num[0])**3 + int(str_num[1])**3 + int(str_num[2])**3 == num:
    print("Your number is Armstrong")
else:
    print("Your number is not armstrong")
