class Solution:

    # 백트래킹과 재귀..
    # Runtime 22.71% Memory 91.54%

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board)
    
    def solve(self, board: List[List[str]])->bool:
        for r in range(len(board[0])):
            for c in range(len(board)):
                if board[r][c] == '.': # 비어있으면
                    for i in range(1,10): # 1부터 9까지 다넣어봄
                        if self.isValid(str(i), r, c, board): # 값이 들어갈 수 있는지 확인함
                            board[r][c] = str(i) # True면 넣음
                            if self.solve(board):
                                return True
                        else: 
                            board[r][c] = '.' # False면 Undo
                    return False
        return True

    def isValid(self, n, r, c, board):
        for i in range(9):
            # 해당 row, col, sub-box 내에 n이 또 있는지 확인한다
            if board[r][i] == n or board[i][c] == n or board[3*(r//3)+(i//3)][3*(c//3)+(i%3)] == n:
                return False
        return True