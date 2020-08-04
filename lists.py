x = [1, 2, 3]
y = [8, 9, 10]

x.append(4)
print(x)

x.extend(y)
print(x)

x.remove(8)
print(x)

x.insert(-1,99)
print(x)

print(len(x))

print([num * 1000 for num in x])