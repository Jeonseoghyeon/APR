jung = '(6+5*(2-8)/2)'
stack_4 = []

prior_st = {
    '(': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
        }
prior_out = {
    '(': 3,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
        }

for i in range(len(jung)):
    if jung[i].isdecimal(): # 피연산자일 때
        print(jung[i],end = ' ')
    
    else: # 연산자일 때
        if len(stack_4) == 0:
            stack_4.append(jung[i])
        else:    
            if jung[i] == ')':
                while stack_4[-1] != '(':
                    x = stack_4.pop()
                    print(x,end =' ')
                stack_4.pop()
                continue
            # print(stack_4)
            
            while stack_4 and prior_out[jung[i]] <= prior_st[stack_4[-1]]:
                y = stack_4.pop()
                print(y, end=' ')
            stack_4.append(jung[i])

while stack_4:
    z = stack_4.pop()
    print(z,end =' ')