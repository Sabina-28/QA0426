#Ask user to input
print("Where should I look")
answer = input()
if answer =="in the bedroom":
    print("Where in the bedroom should I look?")
    answer = input()
    if answer == "under the bed":
        print("Found some shoes, but no phone")
    else :
        print("Found some mess but no phone")
if answer == "in the bathroom":
    print("Where in the bathroom should I look?")
    answer = input()
    if answer == "in the bathtub":
     print("Found a rubber duck but no phone")
    else :
        print("Found bathroom stuff but no phone")
if answer == "in the living room":
    print("Where in the living room should I look?")
    answer = input()
    if answer =="on the table":
        print("Yes! I found my phone")
    else :
        print("Found some stuff but no phone")






