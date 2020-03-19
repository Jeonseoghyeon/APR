import sys
sys.stdin = open("forth_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    numop = input().split()
    ops = ['+','-','*','/','.']
    stack = []
    for i in numop:
        if i in ops:
            if len(stack)>=2:
                if i == '+':
                    x = stack[-1]+stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(x)
                elif i =='-':
                    x = stack[-1]-stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(x)
                elif i =='*':
                    x = stack[-1]*stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(x)
                elif i == '/':
                    x = stack[-1]//stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(x)
            else:
                if i == '.' and len(stack)==1:
                    result = stack[0]
                else:
                    result = 'error'
                    break
                
        else:
            stack.append(int(i))


    print("#{} {}".format(tc,result))
