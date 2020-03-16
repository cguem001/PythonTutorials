fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": " a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
# print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# fruit["pear"] = "great with tequila"
# print(fruit)
# del fruit["lemon"]
# del fruit ---> to delete the whole dictionary
# fruit.clear() ---> to delete the content
print(fruit)
# while True:
#     dict_key = input("please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     # description = fruit.get(dict_key, "We don't have a " + dict_key)
#     # print(description)
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

# for snack in fruit:
#     print(fruit[snack])
# for i in range(10):
#     for snack in fruit:
#         print(snack + ' is ' + fruit[snack])
#     print('-' * 40)

# ordered_key = list(fruit.keys())
# ordered_key.sort()

# ordered_key = sorted(list(fruit.keys()))
# for i in ordered_key:
#     print(i + ' - ' + fruit[i])

# for f in sorted(fruit.keys()):
#     print(f + ' - ' + fruit[f])

# for val in fruit.values(): ---> values is less efficient than keys
#     print(val)
# for keys in fruit.keys(): ---> keys is better than values
#     print(keys)
#
# print(fruit.keys())
# print(fruit.values())
print(fruit)
print(fruit.items())
t_tuple = tuple(fruit.items())
print(t_tuple)

for snack in t_tuple:
    item, description = snack
    print(item + " is(item) " + description + " description")

print(dict(t_tuple))
