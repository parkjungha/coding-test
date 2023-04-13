from collections import deque
from copy import deepcopy

n,m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0 

def bfs():
    global ans
    temp = deepcopy(array)
    q = deque()
    for i in range(n):
        for j in range(n):
            if temp[i][j] == 1: # 벽
                temp[i][j] = '-'

            elif temp[i][j] == 3: # 활성바이러스
                q.append((i,j))
                temp[i][j] = 0

            elif temp[i][j] == 2: # 비활성바이러스
                temp[i][j] = '*'

            elif temp[i][j] == 0: # 빈칸 
                temp[i][j] = '?'

    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if temp[nx][ny] == '?': # 빈칸
                    temp[nx][ny] = temp[x][y]+1 
                elif temp[nx][ny] == '*': # 비활성바이러스
                    temp[nx][ny] = 0 # 활성화
                    q.append((nx,ny))
    

    for i in range(n):
        for j in range(n):
            if temp[i][j].isdigit():
                ans = max(temp[i][j],ans)

def virus(cnt):
    if cnt == m:
        bfs() # 바이러스 전파
        return
    else:
        for i in range(n):
            for j in range(n):
                if array[i][j] == 2: # 바이러스면
                    array[i][j] = 3 # 활성화
                    virus(cnt+1)
                    array[i][j] = 2 # 비활성화 복원

virus(0)
print(ans)