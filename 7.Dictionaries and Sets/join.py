# myList = ["a", "b", "c", "d"]
# letters = "abcdefghijklmnopqrstuvwxyz"
#
# newString = ''
#
# # for d in myList:
# #     newString += d + ","
# # print(newString)
#
# #Instead of doing in the way above we can use join, there's no need to use loop either
# myList = ["a", "b", "c", "d"]
# newString = ",".join(letters)
# print(newString)

locations = {0: "You are sitting in front of a computer learning Python",
             2: "You are standing at the end of a road before a small brick building",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = 1
while True:
    # availableExits = ""
    # for direction in exits[loc].keys():
    #     availableExits += direction + ","
    # Concatenating strings in a loop is not a good practice as it can take lot of space, reducing the performance
    # instead we can do that
    availableExits = ",".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits).upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")
