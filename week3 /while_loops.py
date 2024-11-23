# Ask user response
print("How many numbers should I sum up?")
answer = int(input())

# Declare variables
total_sum = 0
counter = 0
while counter < answer:
    number = int(input(f"Enter number {counter+1}: "))
    total_sum += number
    counter += 1
#Display result
print(f"The answer is {total_sum}")