class Solution:
    # Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
    # from [0][0] to [nrow][ncol]
    # RUNTIME 97.31% (46ms) Memory 84.94% (16.4MB)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        nrow = len(obstacleGrid)
        ncol = len(obstacleGrid[0])

        dp = [[0]*ncol for _ in range(nrow)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0 # 첫번째 칸 장애물이 없으면 1, 있으면 0

        for r in range(1,nrow): # 첫번째 열 초기화 (위에서 아래로)
            if obstacleGrid[r][0] == 0: # 장애물이 없으면
                dp[r][0] = dp[r-1][0] # 윗 칸 값 내려줌
        
        for c in range(1,ncol): # 첫번째 행 초기화 (왼->오)
            if obstacleGrid[0][c] == 0:
                dp[0][c] = dp[0][c-1]
        
        # 그 외 나머지 cell 들 DP matrix construction
        for r in range(1,nrow):
            for c in range(1,ncol):
                if obstacleGrid[r][c] == 0: # 장애물이 없는 경우
                    dp[r][c] = dp[r-1][c] + dp[r][c-1] # 윗 칸 + 왼쪽 칸
        
        return dp[nrow-1][ncol-1]