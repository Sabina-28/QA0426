# Ask user to answer
print("How many bars should be charged?")
answer = int(input())

# Declare a control variable
bars_charged = 0

# Charging
print()

while bars_charged < answer :
    bars_charged = answer + 1
    print(f"Charging {'█' * bars_charged}")
print("The battery is fully charged")