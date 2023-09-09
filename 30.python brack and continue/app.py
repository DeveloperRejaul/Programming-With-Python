# python break and continue
pets = ["docs", "cats", "rabbit"]


# break with for loop
for x in pets:
    print(x)
    if x == "cats":
        break

# break with while loop
i = 0
while i < 5:
    if x == 3:
        break
    print(i)
    i += 1

# python continue statements in for loop
for x in pets:
    if x == "cats":
        continue
    print(x)
# python continue statements in while loop

y = 0
while y < 5:
    if y == 3:
        continue
    print(y)
    y += 1
