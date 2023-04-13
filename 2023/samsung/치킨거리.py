from itertools import combinations
import sys

n, m = map(int,input().split())
all_chicken = []
house = []
for i in range(n):
    a = list(map(int,input().split()))
    for j in range(n):
        if a[j] == 2:
            all_chicken.append((i,j))
        elif a[j] == 1: 
            house.append((i,j))

# m개의 치킨집
minVal = sys.maxsize
remained = combinations(all_chicken, m)

for cand in remained:
    dist_city = 0
    for i, j in house: # 집의 좌표
        dist_house = sys.maxsize
        for x,y in cand: # 치킨집 좌표
            dist_house = min(dist_house, abs(x-i) + abs(y-j))
        dist_city += dist_house
    minVal = min(dist_city, minVal)

print(minVal)