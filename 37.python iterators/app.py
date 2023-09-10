# python iterators
pets = ["dogs", "cat", "rabbit"]

for pet in pets:
    print(pet)

# way 02
iter_pet = iter(pets)
print(next(iter_pet))
print(next(iter_pet))
print(next(iter_pet))
