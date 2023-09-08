class Solution:
    # Run 42.2% (796ms) Mem 48.59% (22.8MB)
    # DP 너무 어렵다 
    def isMatch(self, s, p):
        dp = [[False for _ in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        for i in range(1, len(p)+1):
            if p[i-1] == '*':
                dp[0][i] = True
            else:
                break

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == s[i-1] or p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        return dp[-1][-1]
        
    # Linear search + Backtracking도 어렵다
    def isMatch(self, s, p):
        slen, plen, sidx, pidx, star, curr = len(s), len(p), 0, 0, -1, -1
        while sidx < slen:
            if pidx < plen and p[pidx] in ['?', s[sidx]]:
                pidx += 1
                sidx += 1

            elif pidx < plen and p[pidx] == '*':
                star = pidx
                curr = sidx
                pidx += 1

            else: # elif pidx == plen or p[pidx] != s[sidx]:
                if star == -1:
                    return False
                else: # p는 * 다음, s는 한칸 
                    pidx = star + 1
                    sidx = curr + 1
                    curr = sidx

        return all(p[idx] == '*' for idx in range(pidx, plen)) # 남은 p 모두 *일때만

                