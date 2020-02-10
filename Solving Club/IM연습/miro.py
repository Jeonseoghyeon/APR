import sys
sys.stdin = open("miro_input.txt", "r")

for T in range(1):
    t = int(input())
    arr = []
    for i in range(16):
        arr += [list(map(int, input()))]
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                start = [i, j]
    print(start)
            