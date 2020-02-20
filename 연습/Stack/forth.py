import sys
sys.stdin = open("forth_input.txt","r")

tc = int(input())

for i in range(1,tc+1):
    stack = []
    sample = input().split()
    for x in sample:
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
        print(stack)
    


