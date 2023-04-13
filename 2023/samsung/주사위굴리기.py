from collections import deque

n,m,k = map(int,input().split())
board = []
# visited 필요한가?
for i in range(n):
    board.append(list(map(int,input().split())))

score = 0 # 정답
dice = [1,2,3,4,5,6] # 초기 주사위
dir = 0 # 주사위 첫 방향: 동쪽
currX, currY = 0,0 # 주사위 처음 위치
dx = [0,1,0,-1] # 0 1 2 3 
dy = [1,0,-1,0] # 동 남 서 북

def rotate(d):
    global dice
    if d == 0: # 동
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif d == 1: # 남
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    elif d == 2: # 서
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif d == 3: # 북
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

def move_dice():
    global dir, currX, currY
    nx = currX + dx[dir]
    ny = currY + dy[dir]
    if 0<=nx<n and 0<=ny<m: 
        rotate(dir)
        currX, currY = nx, ny # 주사위 좌표 이동시킴
        return 

    else: # 이동 방향에 칸이 없다면
        dir = (dir+2)%4 # 반대방향
        move_dice()


def calculate_score():
    global score
    B = board[currX][currY] # (x, y)에 있는 정수를 B
    C = 1 # 연속해서 이동할 수 있는 칸의 수 C
    q = deque()
    visited = [[0]*m for _ in range(n)]
    visited[currX][currY] = 1 # 방문표시
    q.append((currX,currY))
    while q:
        x,y = q.popleft()
        for i in range(4): # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == B and visited[nx][ny] == 0: 
                C += 1
                q.append((nx,ny))
                visited[nx][ny] = 1

    score += B*C

def decide_dir():
    global dir
    A = dice[5] # 주사위의 아랫면에 있는 정수 A
    B = board[currX][currY]
    if A>B: # 시계방향 회전
        dir = (dir+1)%4
    elif A<B: # 반시계방향 회전
        dir = (dir-1)%4

# Main
for _ in range(k): # 주사위 이동 k번 반복
    move_dice() # 1. 주사위가 이동 방향으로 한 칸 굴러간다
    calculate_score() # 2. 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다
    decide_dir() #  3. 주사위의 이동 방향을 결정한다.

print(score)