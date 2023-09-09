

# python list type
pets = ["dog", "cat", "rabbit", "mango"]
x = ["god", True, 21]

# indexing
y = pets[0]  # print first data
z = pets[-1]  # print last data

print(z)

# Range of index
d = pets[1:3]
print(d)


# adding items to list
pets.append("mango2")
print(pets)

# insert items specified index
pets.insert(0, "mango3")
print(pets)


# delete items from list
pets.remove("mango2")
print(pets)


# pop method for removing array element
pets.pop()  # like js pop
print(pets)

# also using del key word for remove element
del pets[1]
print(pets)

# getting length of list
x = len(pets)
print(x)


# changing item value
pets[1] = "cat2"
print(pets)


# checking if an items exits
print("cat2" in pets)


# extending List
x = [1, 2, 3]
y = [4, 5, 6]
x.extend(y)
print(x)

# looping through a list
for pet in pets:
    print(pet)


# another way to create list
f = list(("apple", "banana"))
print(f)
