greeting = "hello world"
sides = "$" * 3

hello = "{} {} {}".format(sides , greeting, sides)

top_bottom = "-"  * len(greeting) * 2

print(hello)

print(top_bottom)
print("{}  {}  {}".format(sides , greeting, sides))
print(top_bottom)