from collections import deque
import sys
 
n, m = map(int, input().split())
board = []
for i in  range(n):
    board.append(list(input()))
    for j in range(m):
        if board[i][j] == 'R': # 빨간구슬 위치
            rx, ry = i, j
        elif board[i][j] == 'B': # 파란구슬 위치
            bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]
 
def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    
    visited = []
    visited.append((rx, ry, bx, by))
    
    count = 0
    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            if count > 10: # 움직인 횟수가 10회 초과면 -1 출력
                print(-1)
                return
            
            if board[rx][ry] == 'O': # 현재 빨간 구슬의 위치가 구멍이라면 count출력
                print(count)
                return 
            
            for i in range(4): # 상하좌우 네 방향 탐색
                nrx, nry = rx, ry
                while True: 
                    nrx += dx[i]
                    nry += dy[i]
                    if board[nrx][nry] == '#': # 벽인 경우 왔던 방향대로 한칸 뒤로 이동
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                        
                    if board[nrx][nry] == 'O':
                        break
                        
                nbx, nby = bx, by
                while True: 
                    nbx += dx[i]
                    nby += dy[i]
                    if board[nbx][nby] == '#': # 벽인 경우 왔던 방향대로 한칸 뒤로 이동
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                        
                    if board[nbx][nby] == 'O':
                        break
                        
                if board[nbx][nby] == 'O': # 파란구슬이 구멍에 들어가면 안됨
                    continue
                    
                if nrx == nbx and nry == nby: # 두 구슬의 위치가 같다면
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by): # 이동 거리가 큰 구슬이 구슬 한칸 뒤로 이동
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                        
                if (nrx, nry, nbx, nby) not in visited: # 방문한적이 없는 위치라면
                    q.append((nrx, nry, nbx, nby)) # 큐에 넣고
                    visited.append((nrx, nry, nbx, nby)) # 방문 처리
        count += 1
        
    print(-1) # 10회 안인데 큐에 더이상 아무것도 없는 경우
    
bfs(rx, ry, bx, by)