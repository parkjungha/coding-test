import heapq

def solution(land, height):
    N = len(land)
	
    visited = [[0 for _ in range(N)] for _ in range(N)] # 방문 여부 체크
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    # 우선순위 큐 사용 
    queue = []

    visit_cnt = 0
    max_cnt = N*N
    cost = 0
    queue.append((0, 0, 0)) # 탐색 시작 지점

    while visit_cnt < max_cnt:
        val, x, y = heapq.heappop(queue) # 비용, x좌표, y좌표

        if visited[x][y]: # 이미 방문한 경우 pass
            continue
        visited[x][y] = 1 # 방문 표시 

        visit_cnt += 1
        cost += val # 비용 합산

        curr_height = land[x][y] # 현재 칸 높이

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N: # 범위 벗어나면 pass
                continue
			
            next_height = land[nx][ny] # 다음 칸 높이
            diff = abs(next_height - curr_height) # 현재 칸과 다음 칸의 높이 차이
            if diff > height: # 차이가 height보다 크면 
                heapq.heappush( # 사다리 설치
                    queue, (diff, nx, ny)) # (비용, x좌표, y좌표)
            
            else: # 사다리 필요없다면 비용 0으로 넣어줌
                heapq.heappush(queue, (0, nx, ny))
    return cost
