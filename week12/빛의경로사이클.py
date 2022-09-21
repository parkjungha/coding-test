# 시뮬레이션. 어렵다..

def solution(grid):
    dy = [1, 0, -1, 0]
    dx = [0, -1, 0, 1]
    answer = []
    ly, lx = len(grid), len(grid[0])

    # 각 좌표의 4 방향에 대해서 방문 기록 y*x*4
    visited = [[[0]*4 for _ in range(lx)] for _ in range(ly)]

    for y in range(ly):
        for x in range(lx):
            for d in range(4): # 모든 좌표에 대해서 4방향 탐색
                if visited[y][x][d]: # 해당 좌표-방향이 이미 방문된 경우 -> 사이클 형성
                    continue

                cnt = 0
                ny, nx = y,x
                while not visited[ny][nx][d]:
                    visited[ny][nx][d] = 1
                    cnt += 1
                    if grid[ny][nx] == "S":
                        pass
                    elif grid[ny][nx] == "L": 
                        d = (d-1) % 4
                    elif grid[ny][nx] == "R":
                        d = (d+1) % 4
                    
                    # 현재 방향으로 빛 이동. %로 격자를 벗어난 경우 처리
                    ny = (ny + dy[d]) % ly
                    nx = (nx + dx[d]) % lx

                answer.append(cnt)

    answer = sorted(answer) 
    
    return answer

print(solution(["SL","LR"]))