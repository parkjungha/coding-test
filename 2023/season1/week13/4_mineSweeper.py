class Solution:
    # BFS 단순 구현 
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M': # If a mine 'M' is revealed
            board[click[0]][click[1]] = 'X'
            return board # Game over

        m, n = len(board), len(board[0])
        q = deque()
        q.append((click[0], click[1])) # 시작점

        dx = [-1,1,0,0,1,1,-1,-1] 
        dy = [0,0,-1,1,1,-1,1,-1]
        
        while q:
            x, y = q.popleft()
            temp = []

            if board[x][y] == 'E': # If an empty square 'E'
                cnt = 0 # 지뢰 개수 세기
                for i in range(8): # 모든 방향 탐색
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<m and 0<=ny<n:
                        if board[nx][ny] =='M':
                            cnt += 1
                        temp.append((nx,ny)) # 주변 좌표 temp에 담아둠
 
                if cnt > 0: # with at least one adjacent mine is revealed
                    board[x][y] = str(cnt) # change it to a digit

                else: # with no adjacent mines is revealed
                    board[x][y] = 'B' # change it to a revealed blank 'B'
                    for tx,ty in temp: # adjacent unrevealed squares revealed recursively
                        q.append((tx, ty)) # 주변 좌표 queue에 넣어서 계속 탐색

        return board