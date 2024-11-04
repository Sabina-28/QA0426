#Ask user to input
print("What type of cover does the book have")
cover_type = input()
if cover_type == "soft":
    print("Is the book perfect bound?")
    answer = input()
    if answer == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else :
        print("Soft covers with coil or stitches are great for short books")

else :
    print("Books with hard cover can be more expensive")
