x = [int(input()) for x in range(9)]
x_max = 0
max_i = 0

for i in range(len(x)):
    if x[i]>= x_max:
        x_max = x[i]
        max_i = i

print(x_max)
print(max_i+1)
    
        
