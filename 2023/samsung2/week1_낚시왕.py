# 상어 이동 함수
def move_shark():
    temp = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j]:
                x, y = i, j
                s, d, z = graph[i][j][0]
                dist = s
                # 상어의 속도만큼 1칸씩 이동
                while 0 < dist:
                    nx = x + direction[d][0]
                    ny = y + direction[d][1]
                    # 격자 내부에서 이동하는 경우
                    if 0 <= nx < R and 0 <= ny < C:
                        x, y = nx, ny
                        dist -= 1 # 이동해야 할 남은 거리 1 차감
                    
                    else: # # 벽과 충돌하면 방향 바꿔줌
                        # d(0-1-2-3) : 상-하-우-좌
                        if d == 0 or d == 2:
                            d += 1
                        elif d == 1 or d == 3:
                            d -= 1
                        continue
                temp[x][y].append([s, d, z])

    for i in range(R):
        for j in range(C):
            graph[i][j] = temp[i][j]

# 상어 낚시 함수
def catch_shark():
    global answer
    # 낚시왕 열 한칸 씩 이동 
    for i in range(C):
        for j in range(R):
            # 상어가 존재하는 경우
            if graph[j][i]:
                answer += graph[j][i][0][2]
                graph[j][i].remove(graph[j][i][0])
                break

        move_shark()
        for m in range(R):
            for n in range(C):
                if 1 < len(graph[m][n]): # 한칸에 2마리 이상 있는 경우
                    # 크기 순서대로 상어 제거
                    graph[m][n].sort(key=lambda x: x[2], reverse=True)
                    while 1 < len(graph[m][n]):
                        graph[m][n].pop()

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