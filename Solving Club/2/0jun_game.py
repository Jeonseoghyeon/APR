import sys
sys.stdin = open("0jun_game_input.txt","r")


# S_list = ['S'+'0'+str(x)  if x<10  else 'S'+str(x) for3 x in range(1,14)] # 컴프리헨션으로 카드목록 만들어 줌
tc = int(input())

for i in range(1,tc+1):
    S_count = D_count = H_count = C_count = 13
    cards = input()
    card_list = [cards[x:x+3] for x in range(0,len(cards)-2,3)] # 슬라이싱으로 카드 목록 만들어 줌
    result = ''
    for j in card_list:
        if card_list.count(j)>= 2:
            result = 'ERROR'
            break
        if j[0]=='S':
            S_count -=1
        elif j[0]=='D':
            D_count -=1
        elif j[0]=='H':
            H_count -=1
        elif j[0]=='C':
            C_count -=1
        else:
            pass
        result = '{} {} {} {}'.format(S_count, D_count, H_count, C_count)
    print('#{}'.format(i),result)