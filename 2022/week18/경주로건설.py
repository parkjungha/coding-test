from collections import deque
def solution(board):
    N = len(board)
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    def bfs(x,y,cost,d):
        graph = [[0]*N for _ in range(N)]
        for a in range(N):
            for b in range(N):
                if board[a][b] == 1 : graph[a][b] = -1  # 벽을 -1로 설정
        q = deque()
        q.append((x,y,cost,d))
        while q:
            x,y,cost,idx = q.popleft()
            for i in range(4): # 상하좌우
                nx = x+dx[i]
                ny = y+dy[i]
                if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != -1: # 범위를 벗어나지 않고 벽이 아닐 때
                    if idx == i: # 직진 시에는 직선 도로만 추가되므로
                        newcost = cost + 100
                    else: # 직선 도로 + 코너가 추가되므로
                        newcost = cost + 600

                    if graph[nx][ny] == 0 or ((graph[nx][ny] != 0) and graph[nx][ny] > newcost): # 첫 방문이거나, 재방문인 경우에는 cost가 더 작다면 update
                        q.append((nx, ny, newcost, i)) # 방문시 큐에 담기
                        graph[nx][ny] = newcost # 비용 업데이트 
                    else: continue
        return graph[N-1][N-1]

    return min(bfs(0,0,0,1), bfs(0,0,0,3)) # 시작점에서 아래로 가거나 오른쪽으로 가는 경우