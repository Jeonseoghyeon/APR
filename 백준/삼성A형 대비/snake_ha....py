from copy import deepcopy

def f(stack,direction,blocks):
    global cnt,check
    if direction == 'U':
        for i in range(blocks): # 여기를 잘 정해줘야 한다
            if board[stack[-1][0]-1][stack[-1][1]] !=1:
                stack.append([stack[-1][0]-1,stack[-1][1]])
                stack.pop(0)
                print(stack)
                cnt+=1

            else:
                stack.append([stack[-1][0]-1,stack[-1][1]])
                board[stack[-1][0]][stack[-1][1]] = 0
                print('apple',stack)
                cnt+=1
            if 0 in stack[-1]:
                cnt-=1
                check = 0
                break

# or len(stack)>=4 and (abs(stack[-1][0]-stack[0][0]) == 0 or abs(stack[-1][1] - stack[0][1]) == 0):
    elif direction == 'M':
        for i in range(blocks): # 여기를 잘 정해줘야 한다
            if board[stack[-1][0]+1][stack[-1][1]] !=1:
                stack.append([stack[-1][0]+1,stack[-1][1]])
                stack.pop(0)
                print(stack)
                cnt+=1

            else:
                stack.append([stack[-1][0]+1,stack[-1][1]])
                board[stack[-1][0]][stack[-1][1]] = 0
                print('apple',stack)
                cnt+=1
            if 0 in stack[-1]:
                cnt-=1
                check = 0
                break

    elif direction == 'R':
        for i in range(blocks): # 여기를 잘 정해줘야 한다
            if board[stack[-1][0]][stack[-1][1]+1] !=1:
                stack.append([stack[-1][0],stack[-1][1]+1])
                stack.pop(0)
                print(stack)
                cnt+=1

            else:
                stack.append([stack[-1][0],stack[-1][1]+1])
                board[stack[-1][0]][stack[-1][1]] = 0
                print('apple',stack)
                cnt+=1
            
            if 0 in stack[-1]:
                cnt-=1
                check = 0
                break
    else:
        for i in range(blocks): # 여기를 잘 정해줘야 한다
            if board[stack[-1][0]][stack[-1][1]-1] !=1:
                stack.append([stack[-1][0],stack[-1][1]-1])
                stack.pop(0)
                print(stack)
                cnt+=1

            else:
                stack.append([stack[-1][0],stack[-1][1]-1])
                board[stack[-1][0]][stack[-1][1]] = 0
                print('apple',stack)
                cnt+=1
            if 0 in stack[-1]:
                cnt-=1
                check = 0
                break

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
k = 0
check = 1
d_direction = ['R','M','O','U']
stack = [[1,1]]
for i in range(len(moves)):
    if moves[i][0] == 'D':
        k +=1
    elif moves[i][0] == 'L':
        k-=1
    f(stack,d_direction[k],moves[i][1])
    if check == 0:
        break
    print()
    print()
print(cnt)

