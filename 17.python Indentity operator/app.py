
# python identity operator
# is , is not

# is
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

print(x is y)  # False


x = [1, 2, 3]
y = [1, 22, 3]
z = x
print(z is x)  # true


# is not
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
print(x is not y)  # True


x = [1, 2, 3]
y = [1, 22, 3]
z = x

print(z is not x)  # False
