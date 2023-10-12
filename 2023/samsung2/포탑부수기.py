from collections import deque

def get_attacker():
    tmp = []
    for i in range(n):
        for j in range(m):
            if board[n][m] > 0:
                tmp.append((board[i][j], time[i][j], i+j, j, i))
    tmp.sort(key= lambda x: (x[0], -x[1], -x[2], -x[3]))
    return tmp[0][4], tmp[0][3]

def get_target():
    tmp = []
    for i in range(n):
        for j in range(m):
            if board[n][m] > 0:
                tmp.append((board[i][j], time[i][j], i+j, j, i))
    tmp.sort(key= lambda x: (-x[0], x[1],x[2],x[3])) 
    return tmp[0][4], tmp[0][3]

def attack(x,y,power):
    is_attack[x][y] = 1
    board[x][y] = max(0, board[x][y]-power)

def laser(attackerX,attackerY, targetX, targetY):
    visited = [[0]*m for _ in range(n)]
    track = [[None]*m for _ in range(n)]

    q = deque()
    queue.append((attackerX, attackerY))
    visited[attackerX][attackerY] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = (x + dx[i])%n
            ny = (y + dy[i])%m
            if board[nx][ny] > 0 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = 1
                track[nx][ny] = (x,y)

    if not visited[targetX][targetY]:
        return False

    cx, cy = targetX, targetY
    while (cx,cy) != (attackerX,attackerY):
        power = board[attackerX][attackerY] // 2
        if cx == targetX and cy == targetY:
            power = board[attackerX][attackerY]
        attack(cx,cy,power)
        cx, cy = track[cx][cy]
    return True

def canon(attackerX,attackerY, targetX, targetY):
    attack(targetX, targetY, board[attackerX],board[attackerY])
    dx = [0, 0, -1, -1, -1, 1, 1, 1]
    dy = [-1, 1, 0, -1, 1, 0, -1, 1]

    for i in range(8):
        nx = (targetX + dx[i])%n
        ny = (targetY + dy[i])%m

        if not (nx,ny) == (attackerX, attackerY):
            power = board[attackerX][attackerY]//2
            attack(nx,ny,power)

n,m,k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
time = [[]*m for _ in range(n)]

dx = [0,1,0,-1] # 행
dy = [1,0,-1,0] # 열

def finish():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                cnt += 1

    if cnt == 1:
        return True
    else:
        return False

for t in range(1,k+1):
    if finish():
        break 

    attackerX, attackerY = get_attacker()
    targetX, targetY = get_target()
    board[attackerX][attackerY] += (n+m)
    time[attackerX][attackerY] = t
    is_attack = [[0]*m for _ in range(n)]
    is_attack[attackerX][attackerX] = 1
    if not laser(attackerX,attackerY, targetX, targetY):
        canon(attackerX,attackerY, targetX, targetY)
    
    for i in range(n):
        for j in range(m):
            if not is_attack[i][j] and board[i][j] >0:
                board[i][j] += 1

x,y = get_target()
print(board[x][y])    