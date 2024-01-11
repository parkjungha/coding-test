from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)

# 섬 번호 라벨링
def bfs(x, y):
    visited[y][x] = 1
    arr[y][x] = landNum
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if not visited[ny][nx] and arr[ny][nx]:
                arr[ny][nx] = landNum
                visited[ny][nx] = 1
                q.append((nx, ny))


landNum = 1
for y in range(N):
    for x in range(M):
        if arr[y][x] and not visited[y][x]:
            bfs(x, y)
            landNum += 1

min_distance = [[10**5]*landNum for _ in range(landNum)]

def find_min_distance(landNum):
    dist = [[-1]*M for _ in range(N)]
    q = deque()
    for y in range(N):
        for x in range(M):
            if arr[y][x] == landNum:
                q.append((x, y))
                dist[y][x] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if not dist[ny][nx]: # 같은 섬 번호이면
                continue
            else:
                distance = 1
                while True: # 한칸 씩 이동하면서 
                    nx += dx[i]
                    ny += dy[i]
                    if nx < 0 or nx >= M or ny < 0 or ny >= N:
                        break
                    if not dist[ny][nx]:
                        break
                    if arr[ny][nx] and arr[ny][nx] != landNum: # 다른 섬에 도달
                        if distance > 1: # 최소 거리 갱신
                            min_distance[arr[ny][nx]][landNum] = min(min_distance[arr[ny][nx]][landNum], distance)
                            min_distance[landNum][arr[ny][nx]] = min(min_distance[landNum][arr[ny][nx]], distance)
                        break
                    distance += 1

# 각 섬에서 다른 섬까지 최소 거리 찾아서 min_distance 정보 업데이트
for i in range(1, landNum):
    find_min_distance(i)

costs = []
for i in range(1, landNum):
    for j in range(1, landNum):
        if i > j:
            if min_distance[i][j] != 10**5:
                costs.append((i, j, min_distance[i][j]))
costs.sort(key=lambda x: x[2]) # 거리 순 정렬

price = 0
connected = [0] * landNum
connected[0] = 1
connected[1] = 1
while sum(connected) != landNum:
    for cost in costs:
        s, e, p = cost # 출발 섬, 도착 섬, 최소 거리
        if connected[s] or connected[e]:
            if connected[s] and connected[e]:
                continue
            else:
                connected[s] = 1
                connected[e] = 1
                price += p
                break
    else:
        price = -1
        break

print(price)
