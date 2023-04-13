from collections import deque
m,n = map(int,input().split())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    q = deque()
    q.append([x,y])
    array[x][y]=-2
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 0:
                array[nx][ny] = array[x][y] + 1
                q.append([nx,ny])
                
for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            bfs(i,j)
            
maxVal = -1
for l in array:
    if 0 in l:
        print(-1)
        break
    maxVal= max(maxVal,max(l))

if maxVal == -1: print(0)
else: print(maxVal-1)
