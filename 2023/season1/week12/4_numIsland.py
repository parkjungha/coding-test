class Solution:
    # BFS Runtime 59.14% (308ms) Memory 47.7% (18.6MB)
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid) # 세로
        n = len(grid[0]) # 가로 
        self.ans = 0
        
        def bfs(i,j):
            dx = [-1,1,0,0]
            dy = [0,0,-1,1]
            
            q = deque()
            q.append((i,j))
            grid[i][j] = -1 # 방문 표시
            
            while q:
                x,y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                        grid[nx][ny] = -1
                        q.append((nx,ny)) 
            
            self.ans += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i,j)

        return self.ans

    # DFS
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid) # 세로
        n = len(grid[0]) # 가로 
        dx,dy = [-1,1,0,0], [0,0,-1,1]
        
        def dfs(x,y):
            grid[x][y] = '0'
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                    dfs(nx,ny)
            return 

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    ans += 1
        return ans