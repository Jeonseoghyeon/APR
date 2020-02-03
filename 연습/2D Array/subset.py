'''
bit = [0,0,0,0]

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)
'''

'''
#간결하게 부분집합을 생성하는 방법

arr = [1,2,3]

n = len(arr) #n : 원소의 개수

for i in range(1<<n): # 1<<n : 부분 집합의 개수 (1<<n : 8)
    sub = []
    for j in range(n): # 원소의 수만큼 비트를 비교함 (n = 3)
        if i & (1<<j): # i의 j번째 비트가 1이면 
            sub.append(arr[j]) # j번째 원소 출력
    print(sub)
'''