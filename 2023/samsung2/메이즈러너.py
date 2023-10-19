import copy 

N, M, K = map(int, input().split())

board = [] 
for _ in range(N):
    board.append(list(map(int, input().split())))
    
people = []
for _ in range(M):
    x, y = map(int, input().split())
    people.append([x-1, y-1])

exit = [0]*M

exitX, exitY = map(int, input().split())
exitX -= 1
exitY -= 1

totalMove = 0

def move():
    global people, totalMove
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    for i in range(len(people)):
        if not exit[i]: # 아직 탈출하지 않은 사람
            x, y = people[i]
            currDist = abs(x - exitX) + abs(y - exitY) 

            for k in range(4): # 상하 좌우 돌면서
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                    nextDist = abs(nx - exitX) + abs(ny - exitY)
                    if currDist > nextDist:
                        people[i][0], people[i][1] = nx, ny # 이동
                        totalMove += 1
                        break

        if (people[i][0], people[i][1]) == (exitX, exitY): # 이동한 칸이 출구라면
            exit[i] = 1
            people[i][0], people[i][1] = -1, -1 # 탈출 표시

def checkSquare(x1, y1, x2, y2): # 사각형이 한 명 이상의 참가자와 출구를 포함하는지 
    isExit, isPerson = 0,0
    if x1 <= exitX <= x2 and y1 <= exitY <= y2:
        isExit = 1

    for x, y in people:
        if x1 <= x <= x2 and y1 <= y <= y2 and (x, y) != (exitX, exitY):
            isPerson = 1
            break
    return isExit and isPerson

def findsquare():
    for size in range(1, N):
        for r in range(N):
            for c in range(N):
                x1, y1 = r, c
                x2, y2 = r+size, c+size
                if x2 < N and y2 < N: # 격자 안이면
                    if checkSquare(x1, y1, x2, y2):
                        return x1, y1, x2, y2

def rotate(x1, y1, x2, y2): # 1 0 2 1
    global board, people, exitX, exitY
    # 보드 회전
    temp = [[0]*N for _ in range(N)]
    size = x2-x1+1
    for x in range(N): 
        for y in range(N):
            if x1 <= x <= x2 and y1 <= y <= y2:
                tempX = x - x1
                tempY = y - y1
                newX = tempY
                newY = size - tempX - 1
                temp[newX + x1][newY + y1] = board[x][y]
            else:
                temp[x][y] = board[x][y]
    
    # 회전한 벽 내구도 감소
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if temp[x][y] > 0:
                temp[x][y] -= 1                

    board = temp
#    print(board)
    
    # 사람 회전
    for i in range(len(people)):
        x, y = people[i]
        if x1 <= x <= x2 and y1 <= y <= y2: 
            # (x1,y1) 기준에서 (0,0)으로 변형
            tempX, tempY = x - x1, y - y1
            newX, newY = tempY, size - tempX -1
            people[i][0], people[i][1] = newX + x1, newY + y1
#            print("회전 후", people[i])
    
    # 출구 회전
    if x1 <= exitX <= x2 and y1 <= exitY <= y2: 
        tempX, tempY = exitX - x1, exitY - y1
        newX, newY = tempY, size - tempX - 1
        exitX, exitY = newX + x1, newY + y1

for kk in range(1, K+1): 
    move()

    if sum(exit) == M: # 모든 참가자가 탈출에 성공한다면,
        break # 게임 중단

    x1, y1, x2, y2 = findsquare()
    rotate(x1, y1, x2, y2)

print(totalMove)
print(exitX+1, exitY+1)