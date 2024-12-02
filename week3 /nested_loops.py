#Ask the user a sequence
print("Please enter a sequence")
sequence = input()

#Ask the user to enter a marker
print("Please enter a marker")
marker = input()

#Find the markers
marker1 = -1
marker2 = -1
for position in range(0, len(sequence),1):
    symbol = sequence[position]
    if symbol == marker:
        if marker1 == -1:
            marker1 = position
        else:
            marker2 = position
#Display results
print(f"The distance between the markers is {marker2 - marker1}")