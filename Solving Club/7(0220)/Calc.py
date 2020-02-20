import sys
sys.stdin = open("Calc_input.txt","r")

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
for tc in range(1,11):
    stack_4 = []
    length = int(input())
    jung = input()
    stack_total=[]
    # print(jung)
    for i in jung:
        if i.isdecimal() == 1: # 피연사자일 때
            stack_total.append(i)
            # print(stack_4)
        else: # 연산자일 때
            if i == ')':
                while(stack_4[-1]) != '(':
                    x = stack_4.pop()
                    stack_total.append(x)
                stack_4.pop()
                continue
            while stack_4 and prior_out[i] <= prior_st[stack_4[-1]]:
                 y = stack_4.pop()
                 stack_total.append(y)
            stack_4.append(i)
    while stack_4:
        z = stack_4.pop()
        stack_total.append(z)
    print(stack_total)

    stack = []
    for x in stack_total:
        if x.isdecimal() == 1: # 숫자일 때
            x = int(x)
            stack.append(x)
        elif x =='.': # .일 때
            if len(stack) == 1:
                print("#{} {}".format(i,stack[0]))
            else:
                print("#{} error".format(i))
                break
        else: # 다른 사칙연산일 때
            if len(stack)<2:
                print("#{} error".format(i))
                break
            else:
                if x =='+':
                    z = stack[-2]+stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(z)
                elif x =='-':
                    z = stack[-2]-stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(z)
                elif x == '*':
                    z = stack[-2]*stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(z)
                elif x == '/':
                    z = stack[-2]//stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(z)
                else:
                    pass
    print("#{} {}".format(tc,stack[0]))
    





