def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)] # DP테이블 초기화
    dp[1][1] = 1 # 집

    for i,j in puddles: # 웅덩이가 있는 곳 
        dp[j][i] = -1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if dp[i][j] == -1: # 웅덩이면 패스 
                dp[i][j] = 0
                continue
            
            # 웅덩이가 아니면 왼쪽에서 오는 경우와 위에서 오는 경우를 더해줌 
            dp[i][j] += (dp[i-1][j]+dp[i][j-1]) % 1000000007
    
    return dp[n][m]