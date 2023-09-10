# python sting formatting

x = "I love {} language"
text = x.format("Python")

print(text)

y = "I Love {}, {}, {} language"
text2 = y.format("Python", "javascript", "Dart")
print(text2)


z = "I love {2}, {1}, {0}, Very much"  # index of number
text3 = z.format("Python", "javascript", "HTML")
print(text3)


# using name index
d = "this color {fruit} is {color}"
text4 = d.format(fruit="Banana", color="Red")
print(text4)
