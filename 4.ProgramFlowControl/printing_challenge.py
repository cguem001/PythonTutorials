user = -1
while True:

    if user == 1:
        print("Let's go to Python")
    elif user == 2:
        print("Let's go to Java")
    elif user == 3:
        print("Let's go to swimming")
    elif user == 4:
        print("Let's go to have dinner")
    elif user == 5:
        print("Let's go to bed")
    elif user == 0:
        print("bye bye")
        break
    else:
        print("Please choose your option from the list below")
        print("1. Learn Python")
        print("2. Learn Java")
        print("3. Go swimming")
        print("4. Have dinner")
        print("5. Go to bed")
        print("0. exit")
    user = int(input())
