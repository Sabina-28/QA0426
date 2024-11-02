#Ask user to enter numbers
print("Please enter the first whole number")
number1 = int(input())
print("Please enter the second whole number")
number2 = int(input())
print("Please enter the third whole number")
number3 = int(input())

even_numbers = 0
odd_numbers = 0

# Determine which numbers are even and which are odd
if number1 % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if number2 % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if number3 % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

# Display result
print(f"There were {even_numbers} even and {odd_numbers} odd numbers.")
