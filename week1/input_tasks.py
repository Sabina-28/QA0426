# Ask user to enter their name
name = input("What is your name? ")
# Ask user to enter their age
print("How old are you (in years)?")
age = int(input())
#Ask user their height
print("How tall are you (in meters)?")
height = float(input())
# Ask user their weight
print("How much do you weigh (in kilograms)?")
weight = float(input())
# Calculate the user's bmi
bmi = weight / (height ** 2)
print(f"{name} you are {age} years old and your bmi is {bmi}")