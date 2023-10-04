# 4×4크기 격자, (x, y) x는 행번호, y는 열번호
# 각 물고기는 번호와 방향, 1 <= num <= 16, 방향은 8(상하좌우,대각선)
# 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다. 방향은 (0, 0)에 있던 물고기의 방향과 같다
#############################################
# [물고기 이동] 번호순, 한칸 이동 빈 칸과 다른 물고기가 있는 칸으로 (서로의 위치를 바꿈)
# 상어가 있거나 범위를 벗어나면 이동 X 
# 이동할 수 있을떄까지 45도 반시계 방향 회전
# 이동할 수 있는 칸이 없으면 안함

# [상어 이동] 여러 칸 이동. 
# 물고기가 있는 칸, 물고기를 먹고, 그 방향을 가지게 된다.
# 이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다
# 물고기가 없으면 이동할수없다
# 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1] # 1부터

board = []
fishes = {}
ans = 0

for i in range(4):
    row = list(map(int, input().split()))
    for j in range(0,8,2):  
        fishes[row[j]] = [i,j//2,row[j+1]-1] # fishes[번호] = [x좌표, y좌표, 방향]
    board.append([row[i] for i in range(8) if i%2==0])



def moveFish(currX, currY, currDir):
    for fish in sorted(fishes): # 물고기 번호순
        print(fish,"번 물고기 이동")
        fishX, fishY, fishDir = fishes[fish]
        print("위치", fishX,fishY, "방향",fishDir)

        for i in range(8): # 방향 이동하며 될때까지
            nx = fishX + dx[(fishDir)%8] # 1 + dx[(7+0)%8]=0
            ny = fishY + dy[(fishDir)%8] # 1 + dy[(7+0)%8]=2
            print(nx,ny,"칸 탐색중")
            if nx<0 or nx>=4 or ny<0 or ny>=4 or (nx == currX and ny == currY):
                fishDir += 1
                continue
                
            else: 
                print(board[nx][ny],"물고기가 있던," ,nx,ny, " 칸으로 이동")
                old = board[nx][ny] # 이동할 칸의 물고기 번호
                board[nx][ny] = board[fishX][fishY] # 현재 물고기 한칸 이동
                fishes[fish][0], fishes[fish][1] = nx,ny # 현재 물고기 정보 업데이트
                if old: # 그 칸에 물고기가 있으면 값 바꿔주기
                    board[fishX][fishY] = old
                    fishes[old][0], fishes[old][1] = fishX, fishY
                else: # 빈칸이면 현재 칸 비워줌
                    board[fishX][fishY] = 0 
                break # 한칸 이동후 중단
        fishes[fish][2] = fishDir%8
        print("이동완료")
        print(fishes)

def moveShark(currX, currY, currDir):
    cand = []
    for _ in range(3):
        nx = currX + dx[currDir]
        ny = currY + dy[currDir]
        if 0<=nx<4 and 0<=ny<4 and board[nx][ny]:
            cand.append((nx,ny))
    return cand


def dfs(x,y,eat,board):
    eat += board[x][y]
    currX, currY, currDir = x, y, fishes[board[x][y]][2]
    board[x][y] = -1

    moveFish(currX, currY, currDir)
    cand = moveShark(currX, currY, currDir)
    if cand:
        for nx,ny in cand:
            dfs(nx,ny,eat,board)
    else:
        ans = max(ans,eat)
        return 

dfs(0,0,0,board)
print(ans)

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
# 0  1  2  3  4  5  6  7