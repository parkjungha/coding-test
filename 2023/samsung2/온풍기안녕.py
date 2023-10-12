from collections import deque
import copy

def valid(x, y, visited):
    return 0 <= x < R and 0 <= y < C and visited[x][y] == 0

def bfs(heater, imap):
    cx, cy, d = heater[0], heater[1], heater[2]
    dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)
    visited = [[0 for _ in range(C)] for _ in range(R)]
    q = deque()
    q.append((cx + dx[d - 1], cy + dy[d - 1], 5))
    
    while q:
        x, y, K = q.popleft()
        imap[x][y] += K
        
        if K == 1:
            continue

        if d == 1:
            if valid(x - 1, y + 1, visited) and [x-1, y] not in wall[x][y] and [x-1, y+1] not in wall[x-1][y]:
                visited[x - 1][y + 1] = 1
                q.append((x - 1, y + 1, K - 1))
            if valid(x, y + 1, visited) and [x, y+1] not in wall[x][y]:
                visited[x][y + 1] = 1
                q.append((x, y + 1, K - 1))
            if valid(x + 1, y + 1, visited) and [x+1, y] not in wall[x][y] and [x+1, y+1] not in wall[x+1][y]:
                visited[x + 1][y + 1] = 1
                q.append((x + 1, y + 1, K - 1))
                
        elif d == 2:
            if valid(x - 1, y - 1, visited) and [x-1, y] not in wall[x][y] and [x-1, y-1] not in wall[x-1][y]:
                visited[x - 1][y - 1] = 1
                q.append((x - 1, y - 1, K - 1))
            if valid(x, y - 1, visited) and [x, y-1] not in wall[x][y]:
                visited[x][y - 1] = 1
                q.append((x, y - 1, K - 1))
            if valid(x + 1, y - 1, visited) and [x+1, y] not in wall[x][y] and [x+1, y-1] not in wall[x+1][y]:
                visited[x + 1][y - 1] = 1
                q.append((x + 1, y - 1, K - 1))
                
        elif d == 3:
            if valid(x - 1, y - 1, visited) and [x, y-1] not in wall[x][y] and [x-1, y-1] not in wall[x][y-1]:
                visited[x - 1][y - 1] = 1
                q.append((x - 1, y - 1, K - 1))
            if valid(x - 1, y, visited) and [x-1, y] not in wall[x][y]:
                visited[x - 1][y] = 1
                q.append((x - 1, y, K - 1))
            if valid(x - 1, y + 1, visited) and [x, y+1] not in wall[x][y] and [x-1, y+1] not in wall[x][y+1]:
                visited[x - 1][y + 1] = 1
                q.append((x - 1, y + 1, K - 1))
                
        else:
            if valid(x + 1, y - 1, visited) and [x, y-1] not in wall[x][y] and [x+1, y-1] not in wall[x][y-1]:
                visited[x + 1][y - 1] = 1
                q.append((x + 1, y - 1, K - 1))
            if valid(x + 1, y, visited) and [x+1, y] not in wall[x][y]:
                visited[x + 1][y] = 1
                q.append((x + 1, y, K - 1))
            if valid(x + 1, y + 1, visited) and [x, y+1] not in wall[x][y] and [x+1, y+1] not in wall[x][y+1]:
                visited[x + 1][y + 1] = 1
                q.append((x + 1, y + 1, K - 1))

def calculate_increase(heaters, wall):
    imap = [[0 for _ in range(C)] for _ in range(R)]
    for heater in heaters:
        bfs(heater, imap)
    return imap

def spread():
    global tmap
    dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)
    tmap_copy = copy.deepcopy(tmap)
    
    for x in range(R):
        for y in range(C):
            next_ = []
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
            
                if 0 <= nx < R and 0 <= ny < C and [nx, ny] not in wall[x][y]:
                    next_.append((nx, ny))
                
            for nx, ny in next_:
                diff = abs(tmap[nx][ny] - tmap[x][y])//4
                if tmap[nx][ny] > tmap[x][y]:
                    tmap_copy[x][y] += diff
                elif tmap[nx][ny] < tmap[x][y]:
                    tmap_copy[x][y] -= diff
                    
    tmap = tmap_copy

def decrease():
    global tmap
    for r in range(R):
        for c in range(C):
            if (r == 0 or r == R - 1) or (c == 0 or c == C - 1):
                if tmap[r][c] > 0:
                    tmap[r][c] -= 1



R, C, K = map(int,input().split())

heaters = []
target = []

for i in range(R):
    row = list(map(int,input().split()))
    for j in range(C):
        if 1 <= row[j] <= 4:
            heaters.append([i, j, row[j]])
        elif row[j] == 5:
            target.append([i,j])

wall = [[[] for _ in range(C)] for _ in range(R)] # 각 칸에서 갈 수 없는 곳의 좌표 값 list
W = int(input())

for _ in range(W): 
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1

    if t == 0:
        wall[x][y].append([x-1, y])
        wall[x-1][y].append([x,y])
    elif t == 1:
        wall[x][y].append([x, y+1])
        wall[x][y+1].append([x, y])

tmap = [[0 for _ in range(C)] for _ in range(R)]

ans = 1
increase = calculate_increase(heaters, wall)

while ans <= 100:
    for r in range(R):
        for c in range(C):
            tmap[r][c] += increase[r][c]

    spread()
    decrease()

    if min(tmap[r][c] for r, c in target) < K:
        ans += 1
    else:
        break

print(ans)
