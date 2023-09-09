# python dictionary
person = {
    "firstName": "Rezaul",
    "lastName": "Karim",
    "age": 20
}
print(person)

# accessing items
print(person["age"])
print(person.get("age"))

# adding items
person["hobby"] = "Playing Football"
print(person)


# changing items value
person["firstName"] = "kamal"
print(person)

# removing items
person.pop("age")
print(person)

del person["hobby"]
print(person)


# get len
print(len(person))

# checking if exits
if "age" in person:
    print("the age key exists")
else:
    print("not exists")

# looping
for key in person:
    print(person[key])

# nested dictionary
employees = {
    "manager": {
        "name": "kamal mia",
        "age": 35
    },
    "programmer": {
        "name": "Rezaul Karim",
        "age": 22
    }
}

print(employees["manager"]["name"])
