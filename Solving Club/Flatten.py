import sys
sys.stdin = open("Flatten input.txt","r")

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
        
    print('#{} {}'.format(i+1,max(boxes)-min(boxes)))