import sys
sys.stdin = open("Pascal input.txt","r")

tc = int(input())

for i in range(1,tc+1):
    word = input()
    lw = len(word)

    print('..#.'*(lw)+'.', end='')
    print()
    print('.#'*(lw*2)+'.')

    for x in range(lw):
        print('#',end='')
        print('.{}.'.format(word[x]),end='')

    print('#')
    print('.#'*(lw*2)+'.')
    print('..#.'*(lw)+'.')