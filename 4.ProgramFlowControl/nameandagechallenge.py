age = int(input("Enter your age: "))
name = input("Enter your name: ")

if 18 <= age <= 30:
    print("Welcome to club 18-30 holidays {}".format(name))
else:
    print("Sorry {}, you are not allowed to come".format(name))
