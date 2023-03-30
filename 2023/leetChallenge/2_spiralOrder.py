class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = 0 
        col = 0
        rowEnd = len(matrix)-1
        colEnd = len(matrix[0])-1
        ans = []
        while row <= rowEnd and col <= colEnd:
            for i in range(col, colEnd+1):
                ans.append(matrix[row][i])
            row += 1
            for i in range(row, rowEnd+1):
                ans.append(matrix[i][colEnd])
            colEnd -= 1
            if row <= rowEnd:
                for i in range(colEnd, col-1, -1):
                    ans.append(matrix[rowEnd][i])
                rowEnd -= 1
            if col <= colEnd:
                for i in range(rowEnd, row-1, -1):
                    ans.append(matrix[i][col])
                col += 1
        return ans