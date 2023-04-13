from copy import deepcopy
n,m = map(int,input().split())
A = []
for i in range(n): 
    A.append(list(map(int,input().split())))
moves = []
for i in range(m):
    moves.append(list(map(int,input().split())))
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
clouds = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

def move_cloud(d,s): 
    global clouds, A
    for cloud in clouds: 
        cloud[0] = (cloud[0] + dx[d]*s)%n
        cloud[1] = (cloud[1] + dy[d]*s)%n
        A[cloud[0]][cloud[1]] += 1
    previous = clouds
    clouds = []
    return previous

def magic(previous):
    global clouds, A 
    dix = [-1,-1,1,1]
    diy = [-1,1,-1,1]
    temp = deepcopy(A) 
    visited = [[0]*n for _ in range(n)]
    for cloud in previous:
        x = cloud[0]
        y = cloud[1]
        visited[x][y] = 1
        cnt = 0
        for i in range(4):
            nx = x+dix[i]
            ny = y+diy[i]
            if 0<=nx<n and 0<=ny<n and temp[nx][ny] >0:
                cnt += 1
        A[x][y] += cnt

    # 구름 생성
    for i in range(n):
        for j in range(n):
            if A[i][j]>=2 and not visited[i][j]:
                clouds.append([i,j])
                A[i][j] -= 2 # 물 감소

for d,s in moves: # 이동
    d -= 1
    previous = move_cloud(d,s)
    magic(previous)

ans = 0
for i in range(n):
    for j in range(n):
        ans += A[i][j]

print(ans)