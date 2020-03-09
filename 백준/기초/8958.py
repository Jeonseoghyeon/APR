'''
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
'''

tc = int(input())
for i in range(1,tc+1):
    x = input()
    o_in_a_row = 0
    summ = 0
    for j in x:
        if j =='O':
            o_in_a_row += 1
            summ+=o_in_a_row
        else:
            o_in_a_row = 0
    print(summ)
