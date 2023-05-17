class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordSet = set(wordDict)
        tmp, ans = [],[]

        def dfs(i):
            if i == n:
                res.append(" ".join(tmp))
            for j in range(i,n):
                if s[i:j+1] in wordSet: # 유효한 단어이면
                    tmp.append(s[i:j+1])
                    dfs(j+1) # 그뒤부터 
                    tmp.pop()
        
        dfs(0)
        return res