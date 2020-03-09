challenge = "12345678"

my_iterator = iter(challenge)

for i in range(0, len(challenge)):
    next_item = next(my_iterator)
    print(next_item)
