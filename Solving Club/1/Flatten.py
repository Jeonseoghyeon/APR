import sys
sys.stdin = open("Flatten_input.txt","r")

for i in range(0,10):
    times = int(input())
    boxes = list(map(int,input().split()))

    for dump in range(times): 
        maxx = 1
        minn = 1
        for idx in range(0,len(boxes)):
            if maxx == 1:
                if boxes[idx]== max(boxes):
                    boxes[idx] = boxes[idx] - 1
                    x = boxes[idx] - 1
                    maxx -= 1
            if minn == 1:        
                if boxes[idx] == min(boxes):
                    boxes[idx] = boxes[idx] + 1
                    minn -= 1
            if maxx == 0 and minn ==0:
                break
        
    print('#{} {}'.format(i+1,max(boxes)-min(boxes)))

'''
-maxx,minn 값을 설정해 줌으로써 맥스 -1, 민 +1 할 수 있는 구조를 갖춤

-if maxx == 0 and minn ==0:
                break
 이 코드를 통해 시간을 조금이라도 낮추려 했음

 -그닥 좋은 코드는 아니라는 생각이 든다. 다른사람들과 비교해 봤을 때
'''