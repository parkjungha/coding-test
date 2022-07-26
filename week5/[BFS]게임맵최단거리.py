from collections import deque

def solution(maps):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0] # 상 하 좌 우
    n = len(maps)
    m = len(maps[0])
    
    graph = [[-1 for _ in range(m)] for _ in range(n)] # 
    queue = deque()
    queue.append([0,0]) 
    
    graph[0][0] = 1
    
    while queue:
        y,x = queue.popleft()
        
        # 현재 위치에서 네가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1 and graph[ny][nx] == -1: # 이동할 위치가 범위 안에 있고, 벽이 없는 자리이며, 아직 방문하지 않은 곳일때
                graph[ny][nx] = graph[y][x] + 1 # 방문
                queue.append([ny,nx]) # 
    
    return graph[-1][-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))