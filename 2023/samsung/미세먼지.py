from copy import deepcopy
import sys

input = sys.stdin.readline

r,c,t = map(int,input().split())
array_ = []
air = []
for i in range(r):
    a = list(map(int,input().split()))
    array_.append(a)
    if array_[i][0] == -1: # 공기청정기 위치
        air.append(i)
    
# 1. 미세먼지가 확산된다
def expand():
    global array_
    array = deepcopy(array_)
    # 미세먼지 좌표 queue에 다 담기
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(r):
        for j in range(c):
            if array[i][j] >= 5:
                for n in range(4): # 인접한 네 방향으로 확산
                    nx = i + dx[n]
                    ny = j + dy[n]
                    if 0<=nx<r and 0<=ny<c and array[nx][ny] != -1: # 인접한 방향에 공기청정기가 없고 범위 내에 속하면 확산
                        array[nx][ny] += array_[i][j] // 5 # 인접한 칸에 확산되는 양
                        array[i][j] -= array_[i][j] // 5        

    array_ = array

def clean():
    global array_
    array = deepcopy(array_)

    array[air[0]][1] = 0 # 바람이 나온다
    for i in range(1,c-1): # 0 1 2 ... 6
        array[air[0]][i+1] = array[air[0]][i]
    for i in range(air[0],0,-1): # 2 1 
        array[i-1][-1] = array[i][-1]
    for i in range(c-1, 0, -1): # 7 6 5 ... 1
        array[0][i-1] = array[0][i] 
    for i in range(air[0]-1): # 0 1 
        array[i+1][0] = array[i][0]
    
    array[air[1]][1] = 0 
    for i in range(1,c-1):
        array[air[1]][i+1] = array[air[1]][i]
    for i in range(air[1], r-1):
        array[i+1][-1] = array[i][-1]
    for i in range(c-1, 0, -1): 
        array[-1][i-1] = array[-1][i]
    for i in range(r-1, air[1]+1, -1): # 6 5 
        array[i-1][0] = array[i][0] 

    array_ = array

     
for i in range(t):
    expand()
    clean()

ans = 0
for i in range(r):
    for j in range(c):
        if array_[i][j] > 0:
            ans += array_[i][j]

print(ans)