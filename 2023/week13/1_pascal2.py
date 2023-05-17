class Solution:
    # Run 8.82% (50ms) Mem 15.98% (16.2MB)
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]

        # numRows = 3부터
        ans = [[1]*i for i in range(1, rowIndex+2)] # [[1], [1, 1], [1, 1, 1], ...] 만들어둠
        
        for row in range(2, rowIndex+1):
            for i in range(1, row):
                ans[row][i] = ans[row-1][i-1] + ans[row-1][i]

        return ans[rowIndex]