teman_teman = {
    "Rofiqi":"Informatika",
    "Andika":"Sipil",
    "abdullah":"matematika"
}
friends = teman_teman.copy()
# print(teman_teman)
# print(friends)

# pop() dictionary
dataHilang = friends.pop("Rofiqi")
# print(dataHilang)
# print(friends)

# popitem() dictionary
dataLast = friends.popitem()
# print(dataLast)
# print(friends)