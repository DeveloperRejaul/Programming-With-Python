# python variable scopes
# Global scope
fruit = "banana"


def myFunction():
    global b
    b = "I love python"
    print(fruit)


print(fruit)
myFunction()
print(b)

# Local Scope


def myFunction2():
    a = "hello world"
    print(a)


# print(a) # return error a is not define
myFunction2()
