class Solution:
    # Runtime 5.6% (57ms) Memory 32.43% (16.3MB)
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(m)] # (i,j)까지 가는 unique path 개수 저장
        
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0: # 첫 열, 첫 행은 unique path가 하나
                    grid[row][col] = 1
                else: # 그 외에는 위에서 내려오거나, 왼쪽에서 오거나
                    grid[row][col] = grid[row-1][col] + grid[row][col-1]
        
        return grid[m-1][n-1]
                
class Solution: 
    # Runtime 9.84% (53ms) Memory 32.43% (16.3MB) 비슷비슷
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*(n+1) for _ in range(m+1)]
        
        def dp(r,c):
            if r == 1 or c == 1:
                return 1
                
            if grid[r][c]:
                return grid[r][c]
            
            grid[r][c] = dp(r-1,c) + dp(r,c-1)
            return grid[r][c]
        
        return dp(m,n)