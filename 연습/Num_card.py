import sys
sys.stdin = open("Num_card input.txt","r")

a = int(input())

for i in range(1,a+1):
    max_card_num = 0
    max_card = 0
    card_num = input()
    card_nums = list(map(int,input()))
    for card in card_nums:
        if card_nums.count(card) >= max_card_num:
            if card < max_card:
                continue
            max_card = card
            max_card_num = card_nums.count(card)

    print("#{} {} {}".format(i,max_card, max_card_num))
