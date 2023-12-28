# 상어 이동 함수
def move_shark():
    temp = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j]:
                x, y = i, j
                s, d, z = graph[i][j][0]
                dist = s
                while 0 < dist: # 한칸 씩 이동
                    nx = x + direction[d][0]
                    ny = y + direction[d][1]
                    
                    if 0 <= nx < R and 0 <= ny < C: # 격자 내
                        x, y = nx, ny
                        dist -= 1 # 이동해야 할 남은 거리 --1
                    
                    else: # 벽과 충돌하면 방향 바꿔줌
                        # 0-1-2-3 : 상-하-우-좌
                        if d == 0 or d == 2:
                            d += 1
                        elif d == 1 or d == 3:
                            d -= 1
                        continue

                temp[x][y].append([s, d, z]) # 이동해줌

    for i in range(R):
        for j in range(C):
            graph[i][j] = temp[i][j] # temp 배열 복사

# 상어 낚시 함수
def catch_shark():
    global answer
    # 낚시왕 열 한칸 씩 이동 
    for i in range(C):
        for j in range(R):
            if graph[j][i]: # 현재 칸에 상어가 있으면 
                answer += graph[j][i][0][2] # 잡아먹는다
                graph[j][i].remove(graph[j][i][0]) # 제거
                break

        move_shark() # 모든 상어 이동 
        for m in range(R):
            for n in range(C):
                if 1 < len(graph[m][n]): # 한칸에 2마리 이상 있는 경우
                    graph[m][n].sort(key=lambda x: x[2], reverse=True) # 크기 순 정렬
                    while 1 < len(graph[m][n]):
                        graph[m][n].pop() # 한마리 남을 때까지 제거

if __name__ == '__main__':
    R, C, M = map(int, input().split())
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)] # 상, 하, 우, 좌
    graph = [[[] for _ in range(C)] for _ in range(R)]
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        graph[r-1][c-1].append([s, d-1, z])

    answer = 0
    catch_shark()
    print(answer)