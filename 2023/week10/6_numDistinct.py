class Solution:
    # Run 60.48% (601ms) Mem 69.76% (70.4MB)
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        # number of distinct subsequences of s[0:i] that equals t[0:j].

        # Initialization
        for i in range(m + 1):
            dp[i][0] = 1

        # s, t 한글자씩 보면서 문자가 같을 경우와 다를 경우 두가지 케이스
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]: # s[i]와 t[j] 같을 경우, 두가지 옵션이 가능
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1] # i 선택 안하는 경우 (이전 값 그대로) + i 선택 하는 경우
                else: # 다를 경우, 
                    dp[i][j] = dp[i-1][j] # 이전 값 그대로 참조
        
        return dp[m][n] # 맨 마지막