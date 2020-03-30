def sec_print(field):
    for i in field:
        print(i)
    print()

def play(archor_index):
    global M,N,D
    new_field = [f[:] for f in field]    
    for i in range(3):
        new_field[N][archor_index[i]] = 1 # 궁수 배치 완료
    sec_print(new_field)
    for x in archor_index:
        print(x)
        shoot(N,x,new_field) # 궁수 위치를 부여하여 각각 슛하러 들어가자!
            
        comedown(new_field)



def shoot(y,x,new_field):
    global M,N,D
    min_distance = D+1
    potential_killed=[]
    for i in range(N): # y
        for j in range(M): # x
            if abs(y-i) + abs(x-j) < min_distance and new_field[i][j] == 1: # y:5 x:0,1,2
                min_distance = abs(y-i) + abs(x-j)
                potential_killed = []
                potential_killed.append([i,j])
    print(potential_killed)

def comedown(new_field):
    global M,N,D
    new_field.insert(0,[0]*M)
    new_field.pop(-2)


from itertools import combinations

N,M,D  = map(int,input().split()) # N 행 5, M 열 5, D 공격 거리 제한 1
field = [list(map(int,input().split())) for FIELD in range(N)] + [[0]*M]

archors = list(combinations(range(0,5),3))


for i in archors:
    print(i)
    play(i)