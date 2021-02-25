greeting = "hello world"
sides = "$" * 3

hello = "{} {} {}".format(sides , greeting, sides)

top_bottom = "-"  * len(hello)

print(hello)

print(top_bottom)
print(hello)
print(top_bottom)