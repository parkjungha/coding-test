dx = [0,0,-1,1] # 오 왼 상 하
dy = [1,-1,0,0]

def move(i): # 말 번호
    global horses
    r,c,dir = horses[i]

    nx,ny = r+dx[dir], c+dy[dir] # 이동할 칸

    if not (0<=nx<N and 0<=ny<N) or board[nx][ny] == 2: # 파란색이거나 범위를 벗어날 경우
        # 이동방향 반대 
        if dir == 0: dir =1
        elif dir == 1: dir = 0
        elif dir == 2: dir = 3
        else: dir = 2

        nx,ny = r + dx[dir], c + dy[dir] # 이동할 칸
        horses[i][2] = dir

        if not (0<=nx<N and 0<=ny<N) or board[nx][ny] == 2:
            return False # 해당 말은 더이상 움직일 수 없다

    if board[nx][ny] == 0 or board[nx][ny] == 1: # 흰색 또는 빨간색인 경우
        index = board_horse[r][c].index(i) # 현재 칸에 있는 말들 중에서 몇번째인지
        horse_group = board_horse[r][c][index:] # 현재 말 위에있는 말 모두 함께 이동한다

        if board[nx][ny] == 1: # 빨간색이면 순서 뒤집어져서 이동
            horse_group = horse_group[::-1]

        board_horse[nx][ny] += horse_group # 이동할 칸 list 뒤에 붙여줌

        if horse_group:
            for num in horse_group: # 함께 이동한 말들 위치 좌표 update
                horses[num][0], horses[num][1] = nx,ny
        
        board_horse[r][c] = board_horse[r][c][:index]
        horses[i] = [nx,ny,dir]
    
    for x in range(N):
        for y in range(N):
            if len(board_horse[x][y]) >= 4:
                return True # 네개 모이면 게임 끝
    return False

N,K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
    # 0은 흰색, 1은 빨간색, 2는 파란색

horses = []  # 0번부터 K-1번까지의 말
board_horse = [[[] for _ in range(N)] for _ in range(N)]

for i in range(K):
    r,c,dir = map(int, input().split())
    horses.append([r-1, c-1, dir-1]) 
    board_horse[r-1][c-1].append(i)

turn = 0
end = False

while True:
    if turn > 1000: 
        turn = -1
        break
    if end:
        break
    turn += 1
    for i in range(K):
        if move(i): # 네개 모이면 바로 게임 끝
            end = True
            break 
print(turn)