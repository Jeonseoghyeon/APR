x = input()
x = x.upper()
max_cnt = 0
max_al = ''
y = set(x)
for i in y:
    if x.count(i) > max_cnt:
        max_al = i
        max_cnt = x.count(i)
    elif x.count(i) == max_cnt:
        max_al = '?'
        break
    else:
        pass
print(max_al)