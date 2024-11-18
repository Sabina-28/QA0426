#Ask user to answer
print("How many obstacles should I avoid?")
answer = int(input())

#Declare a control variable
obstacles_avoided = 0

#Avoid obstacles
print()
while obstacles_avoided < answer:
    print("Avoiding ...", end="")
    obstacles_avoided = obstacles_avoided + 1
    print(f"Done! {obstacles_avoided} obstacles avoided.")
