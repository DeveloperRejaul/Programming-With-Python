# python Loop

pets = ["cat", "dogs", "rabbits"]
for pet in pets:
    print(pet)

text = "hello world"
for x in text:
    print(x)

# range
for x in range(5):
    print(x)

# nested for loop
animal = ["tiger", "cat", "dog"]
sound = ["roars", "meows", "barks"]

for x in animal:
    for y in sound:
        print("the " + x + " " + y)


# using else with for
for x in range(5):
    print(x)
else:
    print("loop is done")
