
def solution(grid, d, k):
    n, m = len(grid), len(grid[0])
    dp = [[[0]*(n*m) for _ in range(n*m)] for __ in rage(len(d) + 1)]

    for i in range(n*m):
        dp[0][i][i]= 1
    
    for dd in range(len(d)):
        for i in range(n*m):
            x = i // m
            y = i % m

            for dir in [(-1,0), (0,-1), (0,1), (1,0)]:
                nx = x + dir[0]
                ny = y + dir[1]

                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] - grid[x][y] != d[dd]:
                    for j in range(n*m):
                        dp[dd + 1][j][nx*m + ny] += dp[dd][j][i] % mod
                        dp[dd + 1][j][nx*m + ny] %= mod

https://velog.io/@woolzam/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Lv.4Java-%EA%B2%BD%EC%82%AC%EB%A1%9C%EC%9D%98-%EA%B0%9C%EC%88%98