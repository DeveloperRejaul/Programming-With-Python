# try except
try:
    print(a)
except:
    print("An Error occurred")

txt = "hello world"
print(txt)


# else statement
try:
    a = "hello world"
    print(a)
except:
    print("An Error occurred")
else:
    print("No exception was throw!")


# finally statements
try:
    a = "hello world"
    print(a)
except:
    print("An error occurred")
finally:
    print("Hello, I am still printed")

print("----------------------------------")

try:
    print(b)
except:
    print("An error occurred")
finally:
    print("Hello, I am still printed")


# Throw Error
g = 10

if g > 5:
    raise Exception(" This number is more then 5")
