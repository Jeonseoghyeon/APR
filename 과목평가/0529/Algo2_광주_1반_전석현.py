from itertools import permutations # permutations를 불러준다. 사탕의 갯수 나눠주는 경우의 수를 모두 구하기 위함

T = int(input()) # Test case 개수 받아오기
for tc in range(1,T+1): # Test case 개수만큼 for문 실행
    N,M = map(int,input().split()) # N명의 어린이, M개의 사탕 종류
    max_length = 0 # 초기 max_length 0으로 설정
    children_sweets = [list(map(int,input().split()))[1:] for _ in range(N)] # 아이들이 가지고 있는 사탕을 받아오기

    if M >= N: # 사탕 종류가 아이의 수 이상이면
        give_sweets_category = permutations(range(1,M+1),N) # 모든 경우의 수를 구해서 나누어 줄 것이고,
    else: # 사탕 종류가 아이의 수보다 작으면
        give_sweets_category = permutations(range(1,M+1),M) # 앞의 M명의 어린이에게만 줄 것이다.

    for give_sweet in give_sweets_category: # 나눠줄 경우의수 하나하나 접근하기
        length = 0 # 매번 length가 바뀌어야 하므로 for문 내 length 0으로 설정
        children_sweets_copy = [i[:] for i in children_sweets] # 사탕을 받고 난 뒤 경우의수를 구하기 위해 children_sweets 를 copy해준다(deepcopy보다 빠름)

        if M >= N: # 사탕 종류가 아이의 수 이상이면 
            for give_num in range(N): # 아이의 수만큼 for문을 돌려
                children_sweets_copy[give_num] += [give_sweet[give_num]] # 사탕을 나누어준다.
        else: # 사탕 종류가 아이의 수보다 작으면
            for give_num in range(M): # 종류의 수만큼만 for문을 돌려
                children_sweets_copy[give_num] += [give_sweet[give_num]] # 앞의 M명에게만 사탕을 나누어준다.

        for i in children_sweets_copy: # 나눠받은 뒤 length를 구하기 위해 하나하나 접근
            length += len(set(i)) # set을 써줌으로써 중복된 값이 제거된 종류의 수를 구하자
            if length >= max_length: # max_length 구하기 위한 logic
                max_length = length # max_length 구하기 위한 logic

    print("#{} {}".format(tc,max_length)) # 결과값을 출력해준다.