# import sys
# sys.stdin = open("ver_read input.txt","r")

# tc = int(input())

# for i in range(1,tc+1):
#     x = []
#     for j in range(5):
#         x += [list(input())]
#     y =''
#     max = 0
#     min = min = len(x[0])
#     for mx in range(len(x)):
#         if len(x[mx])>max:
#             max = len(x[mx])
#         if len(x[mx])<min:
#             min = len(x[mx])
    
#     for k in range(max):
#         for l in range(len(x)):
#             if k>=len(x[l]):
#                 y += ''
#             else:
#                 y +=x[l][k]
#     print('#{}'.format(i),''.join(y))

x = [0,1,1,1] *3
print(x)