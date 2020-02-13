import sys
sys.stdin = open("Bracket_input.txt","r")

tc = int(input())
for i in range(1,tc+1):
    stack = []
    result = 1
    x = input()
    # print(x)
    for j in x:
        if j == '(' or j == '{':
            stack.append(j)
        elif j == ')' :
            if len(stack)>0 and stack[-1] =='(':
                stack.pop()
            else:
                result = 0
                break
        elif j == '}' :
            if len(stack)>0 and stack[-1] =='{':
                stack.pop()
            else:
                result = 0
                break
    
    if stack :
        result = 0*result
    else:
        pass
    print("#{} {}".format(i,result))
        