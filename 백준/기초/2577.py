x,y,z = [int(input()) for x in range(3)]
print(x,y,z)

result = str(x*y*z)
print(result)
for i in range(10):
    if i == 0:
        print(result.count('0'))
        continue
    else:
        print(result.count(str(i)))
