import sys
sys.stdin = open("2_input.txt","r")

dx,dy = [0,1,1,1,0,-1,-1,-1],[-1,-1,0,1,1,1,0,-1] # Delta
def dfs(y,x,mine,visit): # dfs 함수 정의
    global min_area, max_amount # min_area, max_amount 값을 전역변수로 가져온다
    cnt = 0 # 1칸인지 아닌지 구분해주기 위한 cnt값
    for i in range(8): # 8방향을 검사해줍니다.
        ny = y + dy[i] # 새로운 y값
        nx = x + dx[i] # 새로운 x값
        if 0<=nx<N and 0<=ny<N and visit[ny][nx] == 0 and mine[ny][nx] == mine[y][x]: # 범위 내에 있고, 주변값이 함수 파라미터값과 같을 때, 방문하지 않았을 때
            cnt+=1 # 카운트 해주고
            break # 브레이크 해줌으로써 이상 필요없는 탐색 안한다.

    if cnt > 0: # 주변에 무언가 있을 때!
        area = 0 # 크기를 세기 위한 변수
        amount = 0 # 양을 세기 위한 변수
        stack = [[y,x]] # 스택에 넣어주고 dfs 시작준비
        while stack: # stack이 비면 멈출것입니다.
            node_y,node_x = stack.pop() # stack에서 해당 노드 위치를 출력
            for i in range(8): #8방향 검사 시작
                ny = node_y + dy[i] #새로운 y값
                nx = node_x + dx[i] #새로운 x값
                if 0<=nx<N and 0<=ny<N and visit[ny][nx] == 0 and mine[ny][nx] == mine[y][x]: # 범위 내에 있고, 주변값이 함수 파라미터값과 같을 때, 방문하지 않았을 때
                    stack.append([ny,nx]) # 해당 값 stack에 추가
                    visit[ny][nx] = 1 # visit처리 해준다.
                    area += 1 # area 크기 1칸 추가
                    amount += mine[y][x] # amount 크기는 해당 노드에 있는 광물의 양만큼 추가

    else: # 주변에 무언가 없으면
        area = 1 # 해당 위치의 크기는 1이고
        amount = mine[y][x] # 양은 해당 위치의 광물의 양이다.
    

    return [amount,area] # 광물의 양과, 크기를 반환해줍니다.

T = int(input()) # 테스트케이스 값 받기

for tc in range(1,T+1): # 테스트케이스 동안
    N = int(input()) # 지도 크기를 받아옵니다.
    mine = [list(map(int,input().split())) for MINE in range(N)] # 광산의 map을 가져옵니다.
    visit = [[0]*N for VISIT in range(N)] # visit를 선언(또 간 곳 안가게 하기 위함)
    min_area = 400 # 가장 작은 area : 문제에서 N의 최대값이 20이라 했으므로 400
    max_amount = 0 # 가장 큰 양을 구하기 위한 max값 설정
    
    #result = [] # amount,area를 받아오기 위한 빈 리스트입니다.
    result = []
    # 아래는 광산을 완전탐색하며 값을 구하지 않은 광산의 범위가 있으면 dfs를 하러 들어가주는 코드입니다.
    for y in range(N):
        for x in range(N):
            if visit[y][x] == 0:
                result.append(dfs(y,x,mine,visit)) # [9,1],[9,3],[1,1],[2,0]
    print(result)
    result.sort() # 결과값을 sort해줍니다.
    
    # 아래는 결과값을 분석하여 max_amount와 min_area값을 구하는 코드입니다.
    for r in range(len(result)-1,-1,-1): # 효율적인 비유를 위해 거꾸로 내려옵니다.
        amount = result[r][0] # 양 값을 받아옵니다.
        area = result[r][1] # 크기 값을 받아옵니다.

        if amount>=max_amount: # max_amount를 구해준다
            max_amount = amount
            if area<=min_area: # min_area를 구해준다
                min_area = area
        # 이 코드를 실행하면 sort된 result의 뒤에서부터 내려오기 때문에 max_amount와 min_area값이 정확하게 나오게 됩니다.
                
    print("#{}".format(tc),max_amount,min_area) #결과값 출력
