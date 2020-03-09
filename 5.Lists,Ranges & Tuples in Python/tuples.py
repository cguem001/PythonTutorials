# # Tuples are immutable, they can't be changed, but a new object can be assigned to a variable

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company" "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984
#
# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[1])
#
# # metallica[0] = "Master of puppets" # the tuple is not possible to be changed
# imelda = imelda[0], "Imelda May", imelda[2]  # an object can be assigned to a variable
# print(imelda)
#
# metallica2 = ["Ride the Lightning", "Metallica", 1984]
# print(metallica2)
#
# metallica2.append("Rock")  # it will be an error because another value was assigned to it and the size is 3
# #
# # title, artist, year = metallica2
# # print(title)
# # print(artist)
# # print(year)
#
# # imelda.append("Jazz") # tuples has no attribute 'append'

# imelda = "More Mayhem", "Imelda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Phyco"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# print(imelda)
#
# album, artist, year, tracks = imelda
#
# print(album, artist, year, tracks)
#
# for songs in tracks:
#     print("\tTrack number: {}, Title: {}".format(songs[0], songs[1]))

imelda = "More Mayhem", "Imelda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Phyco"), (3, "Mayhem"), (4, "Kentish Town Waltz")])

print(imelda)

imelda[3].append((5, "All for you"))

album, artist, year, tracks = imelda

print(album, artist, year, tracks)

for songs in tracks:
    print("\tTrack number: {}, Title: {}".format(songs[0], songs[1]))