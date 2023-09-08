class Solution:
    # Run 94.72% (28ms) Mem 66.41% (14.1MB)
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def DFS(curr, left, right):
            if len(curr) == n*2:
                ans.append(curr)
                return None
            if left < n: 
                DFS(curr + "(", left+1, right)
            if right < left:
                DFS(curr + ")", left, right+1)

        DFS('', 0, 0)
        return ans