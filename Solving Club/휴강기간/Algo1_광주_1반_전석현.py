T = int(input()) # 테스트케이스 수

for tc in range(1,T+1): # 테스트케이스 동안
    N = int(input()) # 총 이동시간
    arr = list(map(int,input().split())) # 10개의 수를 받아온다.
    for i in range(N): # 5번 이동하는 동안

        # 아래는 각각의 경우에 따른 빈 리스트 집합들
        temp_negative_left = [0]*10 # 음수이고 왼쪽으로 벗어날 때
        temp_negative = [0]*10 # 음수일 때
        temp_positive_over10 = [0]*10 # 10 이상의 양수일 때
        temp_positive_under10 = [0]*10 # 10 미만의 양수일 때
        temp_positive_over10_right = [0]*10 # 10 이상의 양수이고 오른쪽으로 벗어날 때
        temp_positive_under10_right = [0]*10 #10 이상의 미만의 양수이고 오른쪽으로 벗어날 때

        for idx in range(len(arr)): # arr의 길이동안
            if arr[idx] < 0: # 해당 인덱스 값이 음수일 때
                if idx-1 <0: # 인덱스 왼쪽으로 벗어날 때
                    temp_negative_left[idx] = (-1) * arr[idx] # 부호 바꿔준 값을 temp에 넣어줌
                else: # 벗어나지 않을 때에는
                    temp_negative[idx-1] = arr[idx] #옆칸으로 옮긴다
            elif arr[idx] > 0: # 해당 인덱스 값이 양수일 때
                if arr[idx] >=10: # 10이상인 양수일 때
                    if idx == 9: # 맨 마지막 칸(오른쪽으로 벗어나는 temp에 넣어줄 것임)
                        temp_positive_over10_right[-2] = -abs(arr[idx]//2) #값을 나누어 넣어준다
                        temp_positive_over10_right[-1] = -abs(arr[idx]//2) #값을 나누어 넣어준다
                    else: # 맨 마지막 칸이 아닐 때(벗어나지 않을 때)
                        temp_positive_over10[idx-1] = -abs(arr[idx]//2) #값을 나누어 넣어준다
                        temp_positive_over10[idx+1] = abs(arr[idx]//2) #값을 나누어 넣어준다
                else:
                    if idx+1 >9: # 맨 마지막 칸(오른쪽으로 벗어나는 temp에 넣어줄 것임)
                        temp_positive_under10_right[idx] = (-1) * arr[idx] # 부호 바꾸고 넣어줌
                    else: #맨 마지막 칸이 아닐 때(벗어나지 않을 때)
                        temp_positive_under10[idx+1] = arr[idx] #값을 넣어줌
            
        for s in range(10): # 각각의 temp들을 합쳐주는 코드
            arr[s] = temp_negative[s]+temp_positive_over10[s]+temp_positive_under10[s]+temp_negative_left[s]+temp_positive_over10_right[s]+temp_positive_under10_right[s]

    # 아래는 결과 출력 코드입니다.
    print("#{}".format(tc),end=' ') 
    for result in arr:
        print(result,end=' ')
    print()
                    
            
        