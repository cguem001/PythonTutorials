fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": " a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print('This is the fruit dictionary ')

veg = {"cabbage": "every child's favourite",
       "sprouts": "mmm, lovely",
       "spinach": "can I have some more fruit, please"}

print(veg)

veg.update(fruit)
print(veg)
print(fruit.update(veg))
print(fruit)
