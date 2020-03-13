#1412 시작 1502 끝
import sys
sys.stdin = open('battlefield_input.txt','r')

def f(location,input,dir):
    global direction,tank,cantgo
    y = location[0]
    x = location[1]
    if keyinput == 'U':
        direction = '^'
        if y-1 >=0 and field[y-1][x] not in cantgo:
            tank = (y-1,x)
            field[y][x] = '.'
            field[y-1][x] = direction
        else:
            field[y][x] = direction
    elif keyinput == 'D':
        direction = 'v'
        if y+1 < H and field[y+1][x] not in cantgo:
            tank = (y+1,x)
            field[y][x] = '.'
            field[y+1][x] = direction
        else:
            field[y][x] = direction
    elif keyinput == 'L':
        direction = '<'
        if x-1 >= 0 and field[y][x-1] not in cantgo:
            tank = (y,x-1)
            field[y][x] = '.'
            field[y][x-1] = direction
        else:
            field[y][x] = direction
    elif keyinput == 'R':
        direction = '>'
        if x+1 < W and field[y][x+1] not in cantgo:
            tank = (y,x+1)
            field[y][x] = '.'
            field[y][x+1] = direction
        else:
            field[y][x] = direction

    elif keyinput == 'S':
        if direction == '^':
            for s in range(y-1,-1,-1):
                if field[s][x] == '*':
                    field[s][x] = '.'
                    break
                elif field[s][x] == '#':
                    break
        elif direction == 'v':
           for s in range(y+1,H):
                if field[s][x] == '*':
                    field[s][x] = '.'
                    break
                elif field[s][x] == '#':
                    break
        elif direction == '<':
            for s in range(x-1,-1,-1):
                if field[y][s] == '*':
                    field[y][s] = '.'
                    break
                elif field[y][s] == '#':
                    break
        elif direction == '>':
            for s in range(x+1,W):
                if field[y][s] == '*':
                    field[y][s] = '.'
                    break
                elif field[y][s] == '#':
                    break

T = int(input())
for tc in range(1,T+1):
    H, W = map(int,input().split()) # H = 4 , W = 6 (격자판 크기)
    field = [list(input()) for f in range(H)] # 배틀필드
    N = int(input())
    keyinputs = input()

    for sero in range(H): # Start 지점 파악
        for garo in range(W):
            if field[sero][garo] in ['<','>','^','v']:
                tank = (sero,garo)
                direction = field[sero][garo]
    
    cantgo = ['*','#','-']
    for key in range(N): # 10
        keyinput = keyinputs[key]
        f(tank,keyinput,direction)

    print("#{}".format(tc),end=' ')
    for y in range(H):
        for x in range(W):
            print(field[y][x],end='')
        print()