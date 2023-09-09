# creating tuple
pets = ("dog", "cat", "rabbit")
print(pets)

x = ("apple", 20, True)
print(x)

# indexing
print(pets[0])
# negative indexing
print(pets[-1])


# range of index
print(pets[1:3])
print(pets[1:])
print(pets[:2])


# getting length of value
print(len(pets))


# looping
for pet in pets:
    print(pet)


# checking if an items exists
print("dog" in pets)


# anther way to create tuple
x = tuple(("mango", "apple"))
print(x)


# combine tuple
d = ("dog", "rabbit")
f = ("cat", "cat2")
x = d + f
print(x)
