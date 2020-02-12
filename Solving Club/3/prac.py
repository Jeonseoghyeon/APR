import copy

x = [1,2,3]
y = copy.deepcopy(x)
y[0] = 3
print(x)
print(y)

print(id(x))
print(id(y))