low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guess = 1
while True:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I get higher or lower? Enter h or l, or c if my guess was correct".format(
        guess).casefold())


    if high_low == "h":

    if high_low == "l":

    elif high_low == "c":
        print("I got it in {} guesses!".format(guess))
    else:
        print("Please enter h, l or c")

