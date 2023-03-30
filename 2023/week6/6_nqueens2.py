class Solution:
    # 75.30%  12.22%
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
        return len(ans)