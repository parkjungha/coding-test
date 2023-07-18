class Solution:
    # Runtime 403ms (86.11%) Memory 19.36mb (58.72%)
    # DFS 탐색 + Memoization 
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        memo = [[0]*n for _ in range(m)] # store the length of the longest increasing path starting from each cell
        ans = 0 # max length

        def dfs(i, j):
            if memo[i][j]:
                return memo[i][j]
            path = 1   # length of the increasing path starting from the current cell
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # 상 하 좌 우
                if 0 <= i+x < m and 0 <= j+y < n and matrix[i+x][j+y] > matrix[i][j]: # 범위에서 벗어나지 않고, increasing일때
                    path = max(path, 1 + dfs(i+x, j+y))   # update max length 
            memo[i][j] = path # current cell의 length of the increasing path를 memoize 
            return path

        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i,j))

        return ans 

