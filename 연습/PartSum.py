import sys
sys.stdin = open("PartSum input.txt","r")

Times = int(input())

for num in range(Times):
    x= list(map(int,input().split()))
    lst_num = [int(x) for x in input().split()] # [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9, 10 ]
    leng = x[0] # 10
    part_leng = x[1] #4
    start = part_leng//2 #2
    end = leng-start #8
    part_max = sum(lst_num[start-start:start+start+1]) #10
    part_min = sum(lst_num[start-start:start+start+1])

    if part_leng %2 == 1:
        for i in range(start, end): 
            if sum(lst_num[i-start:i+start+1]) >= part_max:
                part_max = sum(lst_num[i-start:i+start+1])

            elif sum(lst_num[i-start:i+start+1]) <= part_min:
                part_min = sum(lst_num[i-start:i+start+1])

            else:
                pass
    else:
        for j in range()
        if sum() >= part_max:
            part_max = sum()

        elif sum() <= part_min:
            part_min = sum()

        else:
            pass

    print("#{} {}".format(num+1, part_max-part_min))



