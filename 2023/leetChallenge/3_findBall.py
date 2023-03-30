class Solution:
    # Run 29.78% Mem 48.35%
    def findBall(self, grid: List[List[int]]) -> List[int]:
        if len(grid) == 1 and len(grid[0]) == 1: return [-1]
        answer = [-1 for _ in range(len(grid[0]))]
        for ball in range(len(grid[0])): # 0 1 2 3 4 
            row = 0
            col = ball
            while row < len(grid) and col >= 0 and col < len(grid[0]): # 바닥에 닿을 때 까지
                if grid[row][col] == 1: 
                    col += 1
                    if col < len(grid[0]) and grid[row][col] == -1: # stuck
                        break # 반복문 종료
                    else:
                        row += 1
                else:
                    col -= 1
                    if col > 0 and grid[row][col] == 1: # stuck
                        break
                    else:
                        row += 1
                
                if row == len(grid) and col < len(grid[0]) and col >= 0: # 바닥에 무사히 도달하면
                    answer[ball] = col

        return answer
