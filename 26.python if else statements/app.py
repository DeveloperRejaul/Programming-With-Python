# python if else statements
age = 20

if age > 18:
    print("You are adult person")
else:
    print("You are child person")


# elif
age = 50
if age > 18:
    print("You are adult Person")
elif age > 40:
    print("you are old men")
else:
    print("Nothing ")


# using logical operator
x = 10
y = 5

if (x == 10) and (y == 5):
    print("hello world")


# nested statements
x = 15
if x > 5:
    print("x is more then 5 ")
    if x > 10:
        print("print x is more then 10")
    else:
        print("x is not more then 5")
