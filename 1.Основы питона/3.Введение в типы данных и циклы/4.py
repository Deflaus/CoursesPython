ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

unique = list()
for values in ids.values():
    for value in values:
        if value not in unique:
            unique.append(id)


print(unique)
