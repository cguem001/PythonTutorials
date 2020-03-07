import random

higher = 10
answer = random.randint(1, 10)
print("The answer is {}".format(answer))  # TODO: Remove after testing

print("Please guess number between 1 and {}: ".format(higher))
print("If you press zero the game will be over")
guess = 0

while guess != answer:
    guess = int(input())
    if guess == 0:
        print("Game over")
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Guess higher")
        if guess > answer:
            print("Guess lower")


# if guess == answer:
#     print("You got it first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:   # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
#
