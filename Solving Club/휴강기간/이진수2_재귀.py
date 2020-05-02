import sys
sys.stdin = open("이진수2_input.txt","r")

def my_bin(N,X,cnt,temp):
    global result
    print(cnt,N,X)
    if N == X:
        result=temp
        return 0
    else:
        if cnt>=14:
            return 'overflow'
        else:
            temp1=temp+'1'
            temp2=temp+'0'
            my_bin(N,X+(2**(-cnt)),cnt+1,temp1)
            my_bin(N,X,cnt+1,temp2)


T=int(input())

for tc in range(1,T+1):
    result=''
    num=float(input())
    my_bin(num,0,1,'')

    if result:
        print('#{} {}'.format(tc,result))
    else:
        print('#{} overflow'.format(tc))