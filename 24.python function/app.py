# python function
def myFunction():
    x = "hello world"
    print(x)


myFunction()

# python function parameter / arguments


def hello(name):
    x = "hello " + name
    print(x)


hello("Rezaul Karim")


# multiple parameter
def add_name(name1, name2):
    sum = name1+name2
    print(sum)


add_name("rejaul", "karim")

# python function default permitter


def func(name="Rejaul"):
    x = name
    print(x)


func()
func("kamal")

# keyword arguments


def my_function(name1, name2):
    print("I love" + name1)
    print("I love" + name2)


my_function(name1="rajaul", name2="kamal")


# return statements
def add_nums(num1, num2):
    sum = num1 + num2
    return sum


x = add_nums(5, 4)
print(x)


#
