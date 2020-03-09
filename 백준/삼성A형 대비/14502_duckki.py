from itertools import combinations
from copy import deepcopy
from sys import stdin
import copy

def virus(wall, start):
    global max_safe  # 안전구역 max값을 저장할 변수
    start = deepcopy(start)  # pop을 쓰기 때문에 딥카피
    new_lab = deepcopy(lab)  # 바이러스 퍼뜨리고 다시써야되기 때문에 딥카피
    for i, j in wall:  # 3개의 벽을 세운다
        new_lab[i][j] = 1

    while start:  # bfs를 이용해 바이러스를 퍼뜨림
        y, x = start.pop()
        for k in range(4):
            Y = y + dy[k]
            X = x + dx[k]
            if 0 <= Y < sero and 0 <= X < garo:
                if new_lab[Y][X] == 0:
                    start.append([Y, X])
                    new_lab[Y][X] = 1
    cnt = 0
    for i in range(sero):  # 남은 안전지대를 확인
        for j in range(garo):
            if new_lab[i][j] == 0:
                cnt += 1

    if cnt > max_safe:  # 맥스값과 비교
        max_safe = cnt

    return cnt


sero, garo = list(map(int, input().split()))
lab = [list(map(int, input().split())) for _ in range(sero)]
safe = []
start = []
for i in range(sero):
    for j in range(garo):
        if lab[i][j] == 0:  # 벽이 될 수 있는 곳
            safe.append([i, j])
        elif lab[i][j] == 2:  # 초기 바이러스 위치(시작점)
            start.append([i, j])
            lab[i][j] = 1

safe = list(map(list, combinations(safe, 3)))  # 벽이 될 수 있는 모든 좌표를 3개씩 뽑아서 리스트에 저장

dy = [1, -1, 0, 0]  # 상 하 좌 우
dx = [0, 0, -1, 1]
max_safe = 0
for i in safe:
    virus(i, start)

print(max_safe)