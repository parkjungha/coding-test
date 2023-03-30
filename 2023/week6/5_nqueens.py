class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    DFS(queens+[q], xy_dif+[p-q], xy_sum[p+q])

        result = []
        DFS([],[],[])
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
    
    # Backtracking Runtime 87.89% (50ms) Memory 33.48% (14.4MB)
    def solveNQueens(self, n: int) -> List[List[str]]:
        left, upleft, lowleft = [0]*n, [0]*(2*n-1), [0]*(2*n-1)
        ans = []
        def solve(col, board):
            if col == n:
                ans.append(["".join(i) for i in board])
                return 
            for row in range(n):
                if not left[row] and not upleft[n-1+row-col] and not lowleft[row+col]:
                    board[row][col] = "Q"
                    left[row] = 1
                    upleft[n-1+row-col] = 1
                    lowleft[row+col] = 1
                    solve(col+1, board)
                    board[row][col] = "."
                    left[row] = 0
                    upleft[n-1+row-col] = 0
                    lowleft[row+col] = 0

            board = [["." for i in range(n)] for _ in range(n)]
            solve(0, board)
            return ans