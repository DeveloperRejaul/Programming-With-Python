# python set

# create set using curly brackets
pets = {"dog", "cat", "rabbit"}
print(pets)

x = {"dog", True, 21}

# accessing item
for pet in pets:
    print(pet)

# adding set item
pets.add("mango")
print(pets)

# removing items
pets.remove("rabbit")
print(pets)

# aether removing method
pets.pop()
print(pets)

# get in length set items
print(len(pets))

# cobain tow set
x = {1, 2, 3}
y = {4, 5}
x.update(y)
print(x)


# difference of two sets
x = {1, 2, 3}
y = {4, 2, 8}
print(x-y)
print(y-x)


# create anther way
x = set(("dog", "cat"))
print(x)
