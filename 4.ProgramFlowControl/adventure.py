available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("game over")
        break

<<<<<<< HEAD
print("aren't you glad you got out of there")

for i in range(0, 20):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
=======
else:
    print("aren't you glad you got out of there")
>>>>>>> 6e474b3e2f1965dd5ef0c928203e2b0e42314aee
