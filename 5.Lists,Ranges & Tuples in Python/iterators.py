string = "123456789"

# for char in string:
#     print(char)
# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# if you add more than the number of elements you'll get an error

for char in string:
    print(char)

for char in iter(string):
    print(char)

