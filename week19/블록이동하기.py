from collections import deque

def solution(board):
    N = len(board)
    # 하 우 상 좌
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # (행1, 열1, 로봇 방향, 이동횟수)
    # 방향은 0: 세로 1: 가로
    # 행1, 열1은 로봇의 좌표 중 더 작은 값
    queue = deque([(0,0,1,0)])

    # 방문 기록 (행1, 열1, 로봇 방향)
    visited = set([(0,0,1)]) 

    while queue:
        y1, x1, dir, cnt = queue.popleft()
        y2, x2 = y1 + dy[dir], x1 + dx[dir]

        # 목적지 도착한 경우 반복 중단
        if y2 == N-1 and x2 == N-1: 
            return cnt

        # 네방향 이동
        for d in range(4):
            ny1, nx1 = y1 + dy[d], x1 + dx[d]
            ny2, nx2 = y2 + dy[d], x2 + dx[d]

            # 범위를 벗어나지 않을 때
            if 0 <= ny1 < N and 0 <= nx1 < N and 0 <= ny2 < N and 0 <= nx2 < N:
                if (ny1, nx1, dir) in visited or board[ny1][nx1] == 1 or board[ny2][nx2] == 1: # 이미 방문 했거나, 벽인 경우
                    continue # pass
                # 상하좌우 이동
                queue.append((ny1, nx1, dir, cnt+1))
                visited.add((ny1, nx1, dir))

                # 회전
                rotated_dir = dir^1 # 비트연산자 XOR. 0(세로)이면 1로, 1(가로)이면 0으로 변환
                if dir + d == 1: # 로봇 세로(0)일때 오른쪽(1) 회전, 가로(1)일때 아래쪽(0) 회전하는 경우
                    if (y1, x1, rotated_dir) not in visited: 
                        queue.append((y1, x1, rotated_dir, cnt+1))
                        visited.add((y1, x1, rotated_dir))
                    if (y2, x2, rotated_dir) not in visited:
                        queue.append((y2, x2, rotated_dir, cnt+1))
                        visited.add((y2, x2, rotated_dir))

                elif dir + d == 3: # 로봇 세로(0)일때 왼쪽(3) 회전, 가로(1)일때 위로(2) 회전하는 경우
                    if (ny1, nx1, rotated_dir) not in visited:
                        queue.append((ny1, nx1, rotated_dir, cnt+1))
                        visited.add((ny1, nx1, rotated_dir))
                    if (ny2, nx2, rotated_dir) not in visited:
                        queue.append((ny2, nx2, rotated_dir, cnt+1))
                        visited.add((ny2, nx2, rotated_dir))
    return -1