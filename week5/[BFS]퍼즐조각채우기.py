
dx = [0,0,-1,1]
dy = [1,-1,0,0]

# 조각을 회전시키는 함수
def rotation(puzzle):
    n = len(puzzle)
    m = len(puzzle[0])
    result = [[0]*n for _ in range(m)]
    for r in range(n): 
        for c in range(m):
            result[c][n-1-r] = puzzle[r][c]
    return result

# 퍼즐 찾기. 값이 1인 연결된 묶음을 찾는다
def bfs(i,j,table,check):
    puzzle = []
    n = len(table)
    q = [(i,j)]
    check[i][j] = 1
    while q:
        x,y = q.pop()
        puzzle.append([x,y])
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if not check[nx][ny] and table[nx][ny] == 1:
                q.append((nx,ny))
                check[nx][ny] = 1
    return puzzle

# 찾은 퍼즐의 형태를 저장할 함수
def trans_puzzle(puzzle_location):
    r_min, r_max = 100, -1
    c_min, c_max = 100, -1
    for location in puzzle_location:
        r,c = location
        r_min = min(r_min, r)
        r_max = max(r_max, r)
        c_min = min(c_min, c)
        c_max = max(c_max, c)

    r_len = r_max - r_min +1
    c_len = c_max - c_min +1
    trans = [[0]*c_len for _ in range(r_len)]
    for location in puzzle_location:
        x = location[0] - r_min
        y = location[1] - c_min
        trans[x][y] = 1

    return trans

# 테이블의 빈 곳에 퍼즐을 넣어보고 인접한 칸이 비어있는지 확인하는 함수
def empty_side(game_board, puzzle, i, j):
    n = len(game_board)
    for x in range(len(puzzle)):
        for y in range(len(puzzle[0])):
            if puzzle[x][y] == 1:
                for k in range(4):
                    nx = x+i+dx[k]
                    ny = y+j+dy[k]
                    if not (0 <= nx < n and 0 <= ny < n):
                        continue
                    if game_board[nx][ny] != 1:
                        return True
    return False

# 인접한 칸이 비어있지 않다면 테이블에 조각을 넣고, 아니라면 원 상태로 되돌리는 함수
def is_match(puzzle, game_board):
    n = len(game_board)
    r = len(puzzle)
    c = len(puzzle[0])
    for i in range(n-r+1):
        for j in range(n-c+1):
            match = True
            for x in range(len(puzzle)):
                for y in range(len(puzzle[0])):
                    game_board[x+i][y+j] += puzzle[x][y]
                    if game_board[x+i][y+j] != 1:
                        match = False

            if empty_side(game_board, puzzle, i, j):
                match = False

            if match:
                return True
            else:
                for x in range(len(puzzle)):
                    for y in range(len(puzzle[0])):
                        game_board[x+i][y+j] -= puzzle[x][y]

    return False

def solution(game_board, table):
    n = len(game_board)
    answer = 0
    puzzles = []
    check = [[0] * n for _ in range(n)]
    puzzle_sum = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not check[i][j]:
                puzzle_location = bfs(i, j, table, check) # 퍼즐 조각 찾아서 위치 반환
                puzzle = trans_puzzle(puzzle_location) # 퍼즐 한조각 모양 저장 
                puzzles.append(puzzle)
                puzzle_sum.append(len(puzzle_location)) 

# 조각마다 반복하면서 테이블의 빈공간에 매치시켜봄
    for idx, puzzle in enumerate(puzzles):
        for _ in range(4):
            puzzle = rotation(puzzle)
            if is_match(puzzle, game_board):
                answer += puzzle_sum[idx]
                break

    return answer

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]	))