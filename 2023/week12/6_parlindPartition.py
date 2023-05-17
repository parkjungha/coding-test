class Solution(object):
    ##############################네이버DP문제#################################################
    def minCut(self, s):
        if s == s[::-1]: return 0 # 이미 palindrome 이면 cut = 0 반환
        
        for i in range(len(s)): # 한번 잘랐을 때 
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]: # 두조각 다 palindrome이면 cut = 1 반환
                return 1
      
        dp = [[0 for i in range(len(s))] for j in range(len(s))] # s[i:j+1]가 Palindrome인지 나타내는 boolean matrix 

        for i in range(len(s)):
            for j in range(i, len(s)):
                st = s[i:j+1]
                dp[i][j] = (st == st[::-1])
                      
        # store minimum number of cut for s[0:i]
        res = [0 for _ in range(len(s))] # [0, 0, 0, 0, 0, ... ]
        for i in range(1, len(s)):
            if dp[0][i]: # if 0 to i already Palindrom, no need partition
                res[i] = 0

            else: # find min partition
                minCut = float("inf")
                for j in range(i, 0, -1): # i부터 0까지 감소하면서 확인
                    if dp[j][i]: 
                        minCut = min(minCut, res[j-1]) # 최소값 갱신
                res[i] = minCut + 1

        return res[-1] # 0부터 len(s)까지의 minimum number of partition 반환 