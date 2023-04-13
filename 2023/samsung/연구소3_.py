from collections import deque
import sys
from itertools import combinations

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m = map(int,input().split())
array = []
virus = []
notWall = 0

for i in range(n):
    a = list(map(int,input().split()))
    array.append(a)
    for j in range(n):
        if a[j] == 2: # 바이러스면
            virus.append((i,j)) # 바이러스 좌표 추가
        if a[j] != 1: # 벽이 아니면
            notWall += 1

mvirus = list(combinations(virus,m)) # 전체 바이러스 중에서 m개의 바이러스 조합 리스트

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and array[nx][ny] != 1 and dist[nx][ny]==-1: #범위안에 속하면서 벽이 아닌거
                dist[nx][ny] = dist[x][y]+1
                q.append((nx,ny))
    cnt = 0
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1:
                cnt += 1
    if notWall == cnt:
        maxVal = 0
        for i in range(n):
            for j in range(n):
                if array[i][j] == 0:
                    maxVal = max(maxVal, dist[i][j])
        return maxVal
    return sys.maxsize                

minVal = sys.maxsize
for m in mvirus:
    dist = [[-1]*n for _ in range(n)] # dist 매트릭스 -1로 초기화
    q = deque() # 바이러스 넣을 큐
    for x,y in m: 
        dist[x][y] = 0 # 활성 바이러스는 0
        q.append((x,y)) # 활성 바이러스 queue에다가 넣음
    maxVal = bfs()
    minVal = min(minVal, maxVal) 

print(minVal if minVal!=sys.maxsize else -1)