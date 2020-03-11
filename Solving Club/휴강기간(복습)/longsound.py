import sys
sys.stdin = open('longsound_input.txt','r')

T = int(input())

for tc in range(1,T+1):
    string = str(input()) # 문자열 입력
    H = int(input()) # 하이픈 갯수
    indexes = sorted(map(int,input().split()))
    for i in range(len(indexes)):
        indexes[i] += i
    string_list = []
    for s in range(len(string)):
        string_list.append(string[s])
    for sl in indexes:
        string_list.insert(sl,'-')
    print("#{}".format(tc),end=' ')
    for t in string_list:
        print(t,end='')
    print()
    
