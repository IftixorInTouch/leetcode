string = "123+-21i"

num1 = string.split("+")
print(num1)
print(int(num1[1][:-1]))
