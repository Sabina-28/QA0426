#Ask the user direction
print("What type of adventure should I have?")
answer = input()
if answer == "short":
    print("Entering the dark forest")
elif answer == "long":
    print("Taking the safe route")
else :
    print("Not sure which route to take")