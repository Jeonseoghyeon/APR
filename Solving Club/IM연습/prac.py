import sys
sys.stdin = open("square_input.txt","r")

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# def isplus (j,k):
#     for j in range(N): #x축
#             for k in range(N): # 완전탐색 시작, y축
#                 for l in range(4):
#                     testJ = j + dx[l]
#                     testK = k + dy[l]
#                     if testJ<0 or testK<0 or testJ>N-1 or testK>N-1:
#                         continue
#                     m = arr[testJ][testK]
#                     if m == arr[j][k]+1:
#                         return True
#                     else:
#                         continue
#     return False
                    

tc = int(input())
for i in range(1,1+1): #TC별 시작

    N = int(input()) #정사각형 길이
    arr = []
    max_count = 0
    for lst in range(N):
        arr += [list(map(int,input().split()))]
    print(arr)
    for j in range(N): #x축
        out_count = 0
        count = 0
        for k in range(N): # 완전탐색 시작, y축

            for l in range(4):    
                testJ = j + dx[l]
                testK = k + dy[l]
                if testJ<0 or testK<0 or testJ>N-1 or testK>N-1:
                    continue
                m = arr[testJ][testK]
                if m == arr[j][k]+1:
                    j = testJ
                    k = testK
                    count+=1
# #이동해왔음   
                while 1:    
                    print("여기")
                    for l in range(4):
                        testJ = j + dx[l]
                        testK = k + dy[l]
                        if testJ<0 or testK<0 or testJ>N-1 or testK>N-1:
                            continue 
                        if arr[testJ][testK] == arr[j][k]+1:
                            j = testJ
                            k = testK
                            m = arr[testJ][testK]
                            # count+=1
                        
                            print(m)
                            print(count)
                            print(out_count)
                        
                    
                        else:
                            out_count +=1
                            
                    # if out_count == 4:
                    #     count = 0
                    #     break
                    break
                print()
                print()

                # print(count)
                break #델타를 위한 for문 브레이크



'''
import sys
sys.stdin = open("square_input.txt","r")

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# def isplus (j,k):
#     for j in range(N): #x축
#             for k in range(N): # 완전탐색 시작, y축
#                 for l in range(4):
#                     testJ = j + dx[l]
#                     testK = k + dy[l]
#                     if testJ<0 or testK<0 or testJ>N-1 or testK>N-1:
#                         continue
#                     m = arr[testJ][testK]
#                     if m == arr[j][k]+1:
#                         return True
#                     else:
#                         continue
#     return False
                    

tc = int(input())
for i in range(1,2+1): #TC별 시작

    N = int(input()) #정사각형 길이
    arr = []
    max_count = 0
    for lst in range(N):
        arr += [list(map(int,input().split()))]









    for j in range(N): #x축
        count = 0
        for k in range(N): # 완전탐색 시작, y축
            out_count =0 
            for l in range(4):
                testJ = j + dx[l]
                testK = k + dy[l]
                if testJ<0 or testK<0 or testJ>N-1 or testK>N-1:
                    continue
                m = arr[testJ][testK]
                if m == arr[j][k]+1:
                    j = testJ
                    k = testK
                    count+=1
                    print("여기까진?")
                    while 1:
                        out_count = 0
                        for l in range(4):
                            testJ = j + dx[l]
                            testK = k + dy[l]
                            if testJ<0 or testK<0 or testJ>N-1 or testK>N-1:
                                continue
                            m = arr[testJ][testK]
                            if m == arr[j][k]+1:
                                j = testJ
                                k = testK
                                count+=1
                                print("arr",arr[j][k])
                                print()
                                print("count",count)
                                print()
                            else:
                                out_count += 1
                            if (j,k) == (0,0) or (j,k) == (0,N-1) or (j,k) == (N-1,0) or (j,k) == (N-1,N-1):
                                if out_count == 1:
                                    break
                            elif j == 0 or j == N-1 or k ==0 or k == N-1:
                                if out_count == 2:
                                    break
                            else:
                                if out_count == 3:
                                    break
                        break


                                
                    break
'''
