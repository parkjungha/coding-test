class Solution:
    # Run 70.65% (151ms) Mem 50.34% (17.6MB)
    def minDistance(self, word1: str, word2: str) -> int:
        # DP
        # dp[i][j] = word1[0:i]를 word2[0:j]로 바꾸는 최소 operation 개수 저장
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)] # m*n array

        # Base case 세팅
        # dp[i][0] = word1[0:i]를 empty string으로 바꾸는 operation 개수는 i (delete all)
        # dp[0][j] = empty string을 word2[0:j]로 바꾸는 operation 개수는 j (insert all)
        for i in range(1, m+1): 
            dp[i][0] = i
        for j in range(1,n+1):
            dp[0][j] = j

        # DP 동작
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]: # 두 문자가 같은 경우
                    dp[i][j] = dp[i-1][j-1]
                else: # 다른 경우 replace, delete, insert 중에 최소값 선택
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        return dp[m][n]