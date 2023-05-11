class Solution:
    # DFS 
    # Runtime 30.28% (157ms) Memory 19.35% (18.5MB)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m = len(board) # 세로
        n = len(board[0]) # 가로 

        def dfs(x,y): # 현재 들어온 O 좌표값 (x,y)에 대해서 검사
            dx = [-1,1,0,0]
            dy = [0,0,-1,1]
            board[x][y] = 'N'
            for i in range(4): # 상하좌우 인접한 값
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O': # 범위 안에 속하고 O이면 
                    board[nx][ny] = 'N'
                    dfs(nx, ny) 

        # 경계 먼저 처리함 (경계에 있는 O로부터 시작된 인접한 O들은 모두 변환 불가하므로, 다른 기호(N)로 표시해두기)
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1: # 경계에 있는
                    if board[i][j] == 'O': # O
                        dfs(i,j)

        # 변환 불가능한 O들 모두 따로 표시(N)해준 후, 남은 O들은 변환 가능
        # 모든 좌표 돌면서 O는 X로 변환, N는 O로 복구해줌 - inplace 
        for i in range(m): 
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                elif board[i][j] == 'N':
                    board[i][j] = 'O'
    
    # BFS
    def solve(self, board: List[List[str]]) -> None:
        m = len(board) # 세로
        n = len(board[0]) # 가로 

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        q = deque()

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j] == 'O': # 경계에 있는 O들
                    board[i][j] = 'N' # 따로 표시
                    q.append((i,j)) # 다 Queue에 담음 

        # BFS 탐색으로 경계에 있는 O로부터 인접한 O들은 변환 불가능하므로 N으로 표시해주기
        while q:
            x,y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                    board[nx][ny] = 'N'
                    q.append((nx,ny))

        # 이 부분은 DFS방식과 완전 동일
        for i in range(m): 
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                elif board[i][j] == 'N':
                    board[i][j] = 'O'