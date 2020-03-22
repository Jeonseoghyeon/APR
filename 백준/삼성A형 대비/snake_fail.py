from copy import deepcopy

def f(stack,info):
    direction = info[0]
    blocks = info[-1]
    global cnt
    if direction == 'U':
        for i in range(blocks): # 여기를 잘 정해줘야 한다
            if board[stack[-1][0]-1][stack[-1][1]] !=1:
                stack.append([stack[-1][0]-1,stack[-1][1]])
                stack.pop(0)
                print(stack)
                cnt+=1
                continue
            else:
                stack.append([stack[-1][0]-1,stack[-1][1]])
                print('apple',stack)
                cnt+=1
    elif direction == 'D':
        for i in range(blocks): # 여기를 잘 정해줘야 한다
            if board[stack[-1][0]+1][stack[-1][1]] !=1:
                stack.append([stack[-1][0]+1,stack[-1][1]])
                stack.pop(0)
                print(stack)
                cnt+=1
                continue
            else:
                stack.append([stack[-1][0]+1,stack[-1][1]])
                print('apple',stack)
                cnt+=1

    elif direction == 'R':
        for i in range(blocks): # 여기를 잘 정해줘야 한다
            if board[stack[-1][0]][stack[-1][1]+1] !=1:
                stack.append([stack[-1][0],stack[-1][1]+1])
                stack.pop(0)
                print(stack)
                cnt+=1
                continue
            else:
                stack.append([stack[-1][0],stack[-1][1]+1])
                print('apple',stack)
                cnt+=1
    else:
        for i in range(blocks): # 여기를 잘 정해줘야 한다
            if board[stack[-1][0]][stack[-1][1]-1] !=1:
                stack.append([stack[-1][0],stack[-1][1]-1])
                stack.pop(0)
                print(stack)
                cnt+=1
                continue
            else:
                stack.append([stack[-1][0],stack[-1][1]-1])
                print('apple',stack)
                cnt+=1
    print(cnt,direction)
    return cnt

N = int(input()) # 보드의 크기 N
K = int(input()) # 사과의 개수 K
apples = [list(map(int,input().split())) for ap in range(K)] #사과의 위치

L = int(input()) # 뱀이 방향을 바꾸는 횟수

moves = [input().split() for ap in range(L)]
move = deepcopy(moves)
for i in range(L+1):
    if i == 0:
        moves[i] = ['R',int(move[i][0])]
    elif i == L:
        moves.append([move[i-1][1],10000])
    else:
        moves[i] = [move[i-1][1],int(move[i][0])-int(move[i-1][0])]

board = [[0]*(N+1) for boa in range(N+1)]

for app in range(N+1):
    for le in range(N+1):
        if [app,le] in apples:
            board[app][le] = 1

for bo in range(N+1):
    print(board[bo])

print(moves)
cnt = 0
stack = [[1,1]]
for i in range(len(moves)):
    f(stack,moves[i])
    print()
    print()