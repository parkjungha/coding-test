# 4 × 4 격자 , r행 c열, (1,1)~(4,4)
# 물고기 M마리, 상어 한마리

# 1. 상어가 모든 물고기에게 복제 마법을 시전

# 2. 모든 물고기가 한 칸 이동
#    상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동할 수 없다.
#    이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전
#    이동할 수 있는 칸이 없으면 이동을 하지 않는다. 

# 3. 상어가 연속해서 3칸 이동
#    이동 중 물고기가 있는 칸이면, 그 칸의 모든 물고기는 삭제, 물고기 냄새를 남긴다. 
#    가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동하며
#    여러가지인 경우 사전 순

# 4. 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.

# 5. 1에서 사용한 복제 마법이 완료된다. 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖게 된다.

from copy import deepcopy

M,S = map(int, input().split())
N = 4

# 빈칸 0 물고기 1 상어 -1

fishes = []
fish_board = [[[] for _ in range(N)] for _ in range(4)]

for _ in range(M):
    x,y,d = map(int, input().split())
    fishes.append([x-1, y-1, d-1])
    fish_board[x-1][y-1].append(d-1)

smell = [[0]*4 for _ in range(4)] # 냄새 표시 4x4 격자

sx, sy = map(int, input().split())
sx -= 1
sy -= 1

dx = [0,-1,-1,-1,0,1,1,1] # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dy = [-1,-1,0,1,1,1,0,-1]
dx4 = [-1, 0, 1, 0]
dy4 = [0, -1, 0, 1] # 1 상 2 좌 3 하 4 우

def move_fish(): # 물고기정보, 상어위치, 냄새격자
    res = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while fish_board[x][y]: # 현재 칸에 있는 모든 물고기들 각각 d 방향으로 이동
                d = fish_board[x][y].pop() #현재 물고기의 이동 방향
                for _ in range(8):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (sx, sy) and not smell[nx][ny]:
                        res[nx][ny].append(d)
                        break
                    d = (d-1)%8

                else: # 이동하지 못한 경우는 원상 복구
                    res[x][y].append(d)
    return res

def dfs(x,y, depth, cnt, path):
    global maxCnt, sx, sy, maxPath
    if depth == 3: # 경로가 세개가 채워지면 
        if maxCnt < cnt:
            maxCnt = cnt 
            sx, sy = x, y 
            maxPath = path[:]
        return
        
    for d in range(4):
        nx = x + dx4[d]
        ny = y + dy4[d]
        if 0 <= nx < N and 0 <= ny < N:
            if (nx,ny) not in path:
                path.append((nx, ny))
                dfs(nx, ny, depth+1, cnt + len(fish_board[nx][ny]), path)
                path.pop()
            else:
                dfs(nx, ny, depth+1, cnt, path)


def move_shark():
    dfs(sx, sy, 0, 0, [])
    for x, y in maxPath: # 상어가 이동하는 경로에
        if fish_board[x][y]: # 물고기가 있으면
            fish_board[x][y] = [] # 제거
            smell[x][y] = 3

def smell_remove():
    global smell
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1

def copyMagic():
    for i in range(4):
        for j in range(4):
            fish_board[i][j] += fish_copy[i][j]

###################### MAIN #########################

for _ in range(S):
    # 1. 물고기 복제해둠
    fish_copy = deepcopy(fish_board)
    # 2. 물고기 이동
    fish_board = move_fish()
    # 3. 상어 이동
    maxPath = []
    maxCnt = -1
    move_shark()
    # 4. 냄새 감소
    smell_remove()
    # 5. 복제 마법 수행
    copyMagic()

# 총 물고기의 수 출력
answer = 0
for i in range(4):
    for j in range(4):
        answer += len(fish_board[i][j])

print(answer)
