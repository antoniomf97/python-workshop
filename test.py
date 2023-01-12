a = []
space = [1, 2, 3]

s = space.copy()
a.append((1, s))


s = space.copy()
a.append((1, s))


b = 5 - a[1][1][1]


print(a)
print(b)
