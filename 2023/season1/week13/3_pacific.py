class Solution:
    # Runtime 58.74% (282 ms) Memory 34.1% (17.9MB)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(queue, visited):
            dx = [-1,1,0,0]
            dy = [0,0,-1,1]
            while queue:
                x, y = queue.popleft()
                visited[x][y] = 1
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i] 
                    if 0<= nx <r and 0<= ny <c and not visited[nx][ny]:
                        if heights[nx][ny] >= heights[x][y]: # 물이 흐를 수 있으면
                            queue.append([nx,ny])
                            visited[nx][ny] = 1
                        
        if not heights: return []

        r, c = len(heights), len(heights[0])

        pacific_visited = [[0]*c for _ in range(r)]
        pacific_q = deque()

        atlantic_visited = [[0]*c for _ in range(r)]
        atlantic_q = deque()

        # 경계에 있는 행,열들 담아줌
        for i in range(r): # 첫번째 열, 마지막 열
            pacific_q.append([i,0])
            atlantic_q.append([i,c-1])

        for i in range(c): # 첫번째 행, 마지막 행
            pacific_q.append([0,i])
            atlantic_q.append([r-1,i])
        
        bfs(pacific_q, pacific_visited)
        bfs(atlantic_q, atlantic_visited)

        # 모든 좌표에 대해 둘다 만족하는 좌표값이 정답
        ans = []
        for i in range(r):
            for j in range(c):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    ans.append([i,j])

        return ans