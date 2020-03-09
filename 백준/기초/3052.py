a = []
for i in range(1,11):
    x = int(input())
    a.append(x%42)
a = set(a)
print(len(a))