#Ask user to answer
print("How many apples should I remove?")
answer = int(input())
#Declare a control variable
apples_removed = 10
#Remove apples
print()
while apples_removed < answer:
    print("Removed apple")
    apples_removed = apples_removed + 1

