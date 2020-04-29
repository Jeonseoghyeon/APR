# 1916 시작 2030 끝
import sys
sys.stdin = open("치킨배달_input.txt","r")
from itertools import combinations
N,M = map(int,input().split())
city_map = [input().split() for x in range (N)]
chicken_before = []
for CBy in range(N):
    for CBx in range(N):
        if city_map[CBy][CBx] == '2':
            chicken_before.append([CBy,CBx])
chicken_before_num = len(chicken_before)
chicken_distance = 0 # 치킨 거리의 합
chicken_distance_min = 999999

chicken_after = list(combinations(chicken_before,M)) # 10개의 경우
chicken_after_num = len(chicken_after) # 10
for i in range(chicken_after_num): # 10번 돌릴 것
    city_map_copy = [i[:] for i in city_map] # city_map 복사본
    chicken_list = chicken_after[i] # chicken집 list (2개씩)
    for y in range(N):
        for x in range(N):
            if city_map_copy[y][x] == '2':
                if [y,x] not in chicken_list:
                    city_map_copy[y][x] = '0'
    for y in range(N): 
        for x in range(N):
            if city_map_copy[y][x] == '1':
                cd_min = 999
                for cb in chicken_list:
                    if abs(y-cb[0]) + abs(x-cb[1]) <= cd_min:
                        cd_min = abs(y-cb[0]) + abs(x-cb[1])
                chicken_distance += cd_min
                if chicken_distance > chicken_distance_min:
                    break
    if chicken_distance <= chicken_distance_min:
        chicken_distance_min = chicken_distance
    chicken_distance = 0
    

print(chicken_distance_min)