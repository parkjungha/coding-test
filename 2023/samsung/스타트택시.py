from collections import deque
import sys
input = sys.stdin.readline

n,m,l = map(int,input().split())
array =[]
for i in range(n): # 지도
    array.append(list(map(int,input().split())))

curr_x, curr_y = map(int,input().split()) # 택시 시작 위치
curr_x -= 1
curr_y -= 1
customers = []
for i in range(m): # 승객 출도착 정보
    customers.append(list(map(int, input().split())))

for c in customers:
    for i in range(4):
        c[i] -= 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y): # 현재 택시의 위치에서부터 최단거리 찾기 
    q = deque()
    q.append((x,y))
    dist[x][y] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and dist[nx][ny] == -1 and array[nx][ny] != 1: 
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny))

    minDis = sys.maxsize # 최단거리
    minIdx = 0
    minX, minY = n-1, n-1

    for cus in customers:
        if dist[cus[0]][cus[1]] == -1: # 못태우는 손님이 있다면
            return None

        if dist[cus[0]][cus[1]] < minDis:
            # 최단거리 손님 갱신
            minDis = dist[cus[0]][cus[1]]
            minIdx = customers.index(cus)
            minX, minY = cus[0], cus[1]

        elif dist[cus[0]][cus[1]] == minDis:
            if minX > cus[0]: # 행번호 비교
                minDis = dist[cus[0]][cus[1]]
                minIdx = customers.index(cus)
                minX, minY = cus[0], cus[1]

            elif minX == cus[0]: # 행도 같으면
                if minY > cus[1]: # 열비교
                    minDis = dist[cus[0]][cus[1]]
                    minIdx = customers.index(cus)
                    minX, minY = cus[0], cus[1]

    return minDis, minIdx, minX, minY

failed = False
for i in range(m): # 승객수만큼 반복
    dist = [[-1]*n for _ in range(n)]

    if bfs(curr_x, curr_y) == None: # 시작위치에서 태울 수 없는 손님이 있으면 바로 멈춰
        failed = True
        break 

    # 태울 손님 정보 get
    minDis, minIdx, minX, minY = bfs(curr_x, curr_y)
    l -= minDis # 연료써서 손님한테 감
    
    if l < 0: # 연료 없으면 중단
        failed = True
    curr_x, curr_y = minX, minY # 손님 위치로 택시 이동

    # 이제 승객 태워서 목적지로
    dist = [[-1]*n for _ in range(n)]
    d, u, m, y = bfs(curr_x, curr_y)
    used = dist[customers[minIdx][2]][customers[minIdx][3]] # 승객의 도착지점까지 가는데 필요한 연료
    l -= used

    if l < 0:
        failed = True
    else: # 승객 도착지점 도달
        curr_x, curr_y = customers[minIdx][2], customers[minIdx][3]
        l += used*2 # 연료 충전
        del customers[minIdx] # 완료한 손님 삭제

if len(customers)>0:
    print(-1)
elif failed:
    print(-1)
else:
    print(l)

        