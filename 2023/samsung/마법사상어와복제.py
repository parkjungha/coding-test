from collections import deque

# 물고기 방향
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

# 상어방향
sdx = [-1,0,1,0]
sdy = [0,-1,0,1]

m,s = map(int,input().split())
fish_board = [[[[],[]] for _ in range(4)] for _ in range(4)]
smell_board = [[0]*4 for _ in range(4)]
for _ in range(m):
    x,y,d = map(int, input().split())
    fish_board[x-1][y-1][0].append(d-1)

sx, sy = map(int, input().split())
sx -= 1
sy -= 1
path = []
max_fish_count = -1

visited = [[0]*4 for _ in range(4)]

def solve():
    global path, max_fish_count
    for now in range(s):
        start_copy_fish() # 복제 마법 시전

        move_fish() # 물고기 이동

        path = []
        max_fish_count = -1

        select_move_shark_path(sx,sy,0,0,[])
        move_shark()

        reduce_smell()

        end_copy_fish() # 복제 마법이 완료

    # S번의 연습을 마친 후 격자에 있는 물고기의 수를 출력
    answer = 0
    for x in range(4):
        for y in range(4):
            answer += len(fish_board[x][y][0])

def start_copy_fish():
    for x in range(4):
        for y in range(4):
            for d in fish_board[x][y][0]:
                fish_board[x][y][1].append(d)

def move_fish():
    global fish_board
    move_target = []
    for x in range(4):
        for y in range(4):
            while fish_board[x][y][0]:
                nd = fish_board[x][y][0].pop()
                flag = False
                for i in range(8):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if 0<nx<=4 and 0<ny<=4:
                        move_target.append((nx,ny,nd)) # 이동한다
                        flag = True
                        break
                    nd = (nd-1)%8 # 방향 45도 반시계 회전

                if not flag: # 이동할 수 없으면 움직이지 않는다
                    move_target.append((x,y,nd)) 

    for x,y,nd in move_target: # 이동시켜줌
        fish_board[x][y][0].append(nd)

    
def select_move_shark_path(x,y,fish_count,move_count,tmp_path):
    global visited, max_fish_count, path
    if move_count == 3: # DFS 종료조건
        if max_fish_count < fish_count:
            max_fish_count = fish_count
            path = [d for d in tmp_path] # 최대로 먹을 수 있는 방향으로 결정해줌
        return 

    # 상어가 갈수있는 네방향
    for d in range(4):
        nx = x + sdx[d]
        ny = y + sdy[d]
        if 0<=nx<4 and 0<=ny<4:
            if not visited[nx][ny]: # 방문하지 않았으면
                visited[nx][ny] = 1
                nxt_fish_count = fish_count + len(fish_board[nx][ny][0]) # 이 자리에 있는 fish 먹어줌
                select_move_shark_path(nx, ny, nxt_fish_count, move_count+1, tmp_path+[d])
                visited[nx][ny] = 0
            if visited[nx][ny]: # 이미 방문했어도 다시 갈 수 있다. 물고기는 못먹음
                select_move_shark_path(nx, ny, fish_count, move_count+1, tmp_path+[d])

def move_shark():
    global sx, sy, fish_board, smell_board
    for d in path: # 상어 이동시킴
        sx += sdx[d]
        sy += sdy[d]
        if fish_board[sx][sy][0]: # 물고기 있으면 먹음
            fish_board[sx][sy][0] = []
            smell_board[sx][sy] = 3 # 냄새 남겨줌
    
def reduce_smell():
    global smell_board
    for x in range(4):
        for y in range(4):
            if smell_board[x][y] > 0:
                smell_board[x][y] -= 1

def end_copy_fish():
    global fish_board
    for x in range(4):
        for y in range(4):
            while fish_board[x][y][0]:
                fish_board[x][y][0].append(fish_board[x][y][1].pop())

solve()