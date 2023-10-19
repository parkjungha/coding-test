n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

target = []
for _ in range(m):
    x, y = map(int, input().split())
    target.append([x-1, y-1])

arrived = [0]*m # i 번째 사람이 도착했으면 1, 아직이면 0
people = [[-1, -1] for _ in range(m)] # 격자 내에 있는 사람들의 좌표 리스트
block = [[0]*n for _ in range(n)] # 갈 수 없는 칸 격자

from collections import deque

def getPath(sx, sy, tx, ty): # (sx, sy)부터 (tx, ty)까지 최단거리 경로의 좌표들 list 반환

    dx = [-1, 0, 0, 1] # 우선순위
    dy = [0, -1, 1, 0]

    visited = [[0]*n for _ in range(n)]
    visited[sx][sy] = 1
    q = deque()
    q.append((sx, sy, [(sx, sy)])) # 시작점

    while q:
        x, y, path = q.popleft()

        if (x,y) == (tx, ty): # 목적지에 도달하면
            return path # 경로 반환

        for i in range(4): # 아직이면 상하좌우 인접한 칸 돌면서 탐색
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and not block[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny, path + [(nx, ny)]))


def movePeople():
    global people, block, arrived

    for i in range(m):
        x, y = people[i]
        tx, ty = target[i]
        if (x,y) == (-1, -1) or (x,y) == (tx, ty): # 아직 격자 밖이면
            continue
        path = getPath(x, y, tx, ty)
        nx, ny = path[1]
        people[i][0], people[i][1] = nx, ny

    # 사람들이 모두 이동한 뒤에, 칸 block
    for i in range(m):
        if not arrived[i] and people[i] == target[i]: # 편의점에 도착한다면
            block[people[i][0]][people[i][1]] = 1 # 더이상 못지나감
            arrived[i] = 1 # i번째 사람 도착 표시


def enterBase(i): # i번째 사람이 베이스캠프에 들어감
    global people, block
    
    tx, ty = target[i] # 가고싶은 편의점

    minLen = float('inf')
    minPath = []
    
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1 and not block[x][y]: # 막히지 않은 베이스캠프라면

                currPath = getPath(x, y, tx, ty)
                if currPath == None: # 경로가 없는 것
                    continue
                if minLen > len(currPath): # 현재 경로 길이가 더 작으면
                    minLen = len(currPath) # 최단 경로 정보 갱신
                    minPath = currPath
                # 같으면 갱신하지 않는다 -> 자동으로 우선순위대로 행 열 작은 베이스캠프 정보가 유지됨
    
    baseX, baseY = minPath[0]
    people[i][0], people[i][1] = baseX, baseY
    block[baseX][baseY] = 1
    
time = 0
while True:
    time += 1
    if sum(arrived) == m: # 모든 사람이 도달
        time -= 1
        break

    movePeople()


    for i in range(1, m+1):
        if i == time: # i번째 사람이 현재 time에 들어갈 때면
            enterBase(i-1)

print(time)