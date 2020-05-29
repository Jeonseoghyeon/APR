def is_working(y,x,num): # 숫자를 넣어준 뒤 스도쿠가 성립하는지 확인해주는 함수
    global cnt, flag # main 함수로부터 cnt, flag 값을 가져와준다

    if flag == True: # flag를 써줌으로써 스도쿠가 성립하지 않은 이후의 상황에 대해서는 함수가 실행되지 않도록(input 받아오는 오류를 해결해줘야하기 때문)
        start_y, start_x = ((y//3)*3),((x//3)*3) 
        # 숫자가 들어가는 y,x 위치와 number를 설정해준다. ex) 1,0이면 0,0부터 2,2까지 찾아야하므로 start_x = 0, start_y = 0

        for ver_y in range(9): # 수직(열) 검사
            if ver_y != y: # 들어온 위치의 y좌표 제외
                if arr[ver_y][x] == num: # 들어온 값이 열 내에 있을 경우
                    flag = False # flag False 처리
                    return
        
        for ver_x in range(9): # 수평(행) 검사
            if ver_x != x: # 들어온 위치의 x좌표 제외
                if arr[y][ver_x] == num: # 들어온 값이 행 내에 있을 경우
                    flag = False # flag False 처리
                    return
        
        # 이 부분은 해당 block 안에 들어오게 된 num과 같은 수가 있는지 검사해준다.
        for block_y in range(start_y,start_y+3): # 검색해줄 block의 y좌표 범위 설정
            for block_x in range(start_x,start_x+3): # 검색해줄 block의 x좌표 범위 설정
                if block_y != y and block_x != x: # 들어온 위치의 좌표 제외
                    if arr[block_y][block_x] == num: # 들어온 값이 block 내에 있을 경우
                        flag = False # flag False 처리
                        return

        cnt+=1 # 모든 검사를 수행한 경우 cnt를 +1 해준다.
    
# main 함수
T = int(input()) # Test case 개수 받아오기

for tc in range(1,T+1): # Test case 개수만큼 for문 실행
    N = int(input()) # y,x좌표 및 들여올 숫자 set의 개수 N 받아오기
    arr = [list(map(int,input().split())) for _ in range(9)] # 스토쿠 판 받아오기
    cnt = 0 # 초기 cnt값 0으로 설정
    flag = True # 초기 flag값 True로 설정
    for put_num in range(N): # 숫자를 순차적으로 넣기 시작
        y,x,num = list(map(int,input().split())) # y,x좌표 및 들여올 숫자를 받아준다.
        arr[y][x] = num # 해당 좌표에 해당 값을 넣어준다.
        is_working(y,x,num) # 이후 스도쿠가 알맞게 동작하는지 확인
            
    print("#{} {}".format(tc,cnt)) # 결과값을 출력해준다.