class Solution:
    # Dynamic Programming -> 점화식 잘찾기 .. 
    
    #Runtime 21.5%(69ms) Memory 43.39% (16.5MB)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        
        # dp[i][j] = s1[0:i]와 s2[0:j]로 s3[0:i+j]를 만들 수 있다면 True, 아니면 False
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True # Initialization (i=0, j=0일때)

        # 점화식
        # s1와 s3의 마지막 character 같으면 이전 값 dp[i-1][j] 체크
        # s2와 s3의 마지막 character 같으면 이전 값 dp[i][j-1] 체크
        for i in range(m+1):
            for j in range(n+1):
                if i>0 and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j] or dp[i][j]
                if j>0 and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j-1] or dp[i][j]

        return dp[m][n]