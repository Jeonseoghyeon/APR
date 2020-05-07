import sys
sys.stdin = open("베이비진_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    cards = list(map(int,input().split()))
    result = 0
    flag = False
    player1 = []
    player2 = []
    for i in range(12):
        if i % 2 == 0 :
            player1.append(cards[i])
            player1.sort()
        else :
            player2.append(cards[i])
            player2.sort()
        len_1 = len(player1)
        len_2 = len(player2)
        player_1_set = list(set(player1))
        player_2_set = list(set(player2))
        if len_1 >= 3:
            for i in range(len_1):
                if player1.count(player1[i]) == 3:
                    result = 1
                    flag = True
        if len(player_1_set) >= 3:
            for i in range(len(player_1_set)):
                if player_1_set[i] - player_1_set[i-1] == 1 and player_1_set[i-1] - player_1_set[i-2] == 1:
                    result = 1
                    flag = True

        if flag == True:
            break
        if len_2 >= 3:
            for i in range(len_2):
                if player2.count(player2[i]) == 3:
                    result = 2
                    flag = True
        if len(player_2_set) >= 3:
            for i in range(len(player_2_set)):
                if player_2_set[i] - player_2_set[i-1] == 1 and player_2_set[i-1] - player_2_set[i-2] == 1:
                    result = 2
                    flag = True
        if flag == True:
            break

    print("#{} {}".format(tc,result))

    