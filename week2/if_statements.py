#Ask user to enter numbers
print("Please enter the first number")
number1 = int(input())
print("Please enter the second number")
number2 = int(input())
if number1 > number2:
    print("The first number is greater than the second number")
elif number1 < number2:
    print("The second number is greater than the first number")
else:
    print("The numbers are equal")
