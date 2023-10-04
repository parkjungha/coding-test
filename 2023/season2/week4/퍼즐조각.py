from collections import defaultdict
from collections import deque

def bfs(i, j, table, visited, target):
    n = len(table)
    q = deque()
    q.append((i,j))
    block = set([(0,0)])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if table[nx][ny] == target and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    block.add((nx-i, ny-j)) # 0,0 기준으로 값 빼서 좌표 저장
    return block

def fill_block(empty_block, puzzles, n):
    for _ in range(4): # 블럭을 네 방향으로 회전
        dx, dy = min(empty_block) # 빈칸 영역 중 가장 왼쪽 위에 값
        new_info = set()
        for x,y in empty_block: # 빈칸 하나씩 돌면서
            new_info.add((x-dx, y-dy)) # 시작 좌표를 0,0으로 맞춰줌
        if new_info in puzzles: # 퍼즐과 빈칸이 동일하면
            puzzles.remove(new_info) # 해당 퍼즐 사용
            return len(new_info)

        empty_block = rotate_block(empty_block, n) # 안맞으면 회전
    
    return 0 # 해당 빈칸 영역에 채워지는게 없으면 

def rotate_block(empty_block, n): # 오른쪽으로 90도 회전
    new_info = set()
    for x,y in empty_block:
        new_info.add((y, n-x-1)) # Rotate !!!!!!!!!!!
    return new_info

def solution(game_board, table):
    answer = 0
    n = len(table)
    
    # 1. Table에서 퍼즐 조각 정보 찾기
    visited = [[0]*n for _ in range(n)]
    puzzles = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and visited[i][j] == 0: # 방문하지 않은 블럭이면
                visited[i][j] = 1
                puzzle = bfs(i,j,table,visited,1) # 현재 퍼즐 모양 가져오기
                puzzles[len(puzzle)].append(puzzle) # 퍼즐 조각의 크기별로 위치정보 저장

    # 2. Game board에서 빈칸 정보 찾기
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0 and visited[i][j] == 0:
                visited[i][j] = 1
                empty_block = bfs(i,j,game_board,visited,0) # 현재 빈칸 영역 가져오기
                if len(empty_block) in puzzles: # 크기가 동일한 퍼즐에 대해서 채울수있는지 확인함
                    canFill = fill_block(empty_block, puzzles[len(empty_block)], n) # 채울수있는 블럭 개수
                    answer += canFill
    return answer