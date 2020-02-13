import sys
sys.stdin = open('Repeated_input.txt','r')

tc = int(input())

for i in range(1,tc+1):
    arr = list(input())  # ABCCB
    stack = []
    for x in arr:
        stack.append(x)
        if len(stack)>=2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
    print("#{} {}".format(i,len(stack)))      