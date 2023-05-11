class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1],[1,1]]

        # numRows = 3부터
        ans = [[1]*i for i in range(1, numRows+1)] # [[1], [1, 1], [1, 1, 1], ...] 만들어둠
        
        for row in range(2, numRows):
            for i in range(1, row):
                ans[row][i] = ans[row-1][i-1] + ans[row-1][i]

        return ans