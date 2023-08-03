class Solution:
    # Run 545ms (99.97%) Memory 23.51mb (90.23%)
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [0] * n # 0: 방문안함, 1: 방문함, 2: terminal node
        ans = []

        def isSafe(node):
            if visited[node] != 0: # 이미 방문된 경우
                return visited[node] == 2 # terminal node인지 
            
            visited[node] = 1 # 방문 표시
            for neighbor in graph[node]: # 이웃 탐색 
                if not isSafe(neighbor): # 재귀 (False-> safe node가 아님)
                    return False
            
            visited[node] = 2 # 모든 이웃이 safe인 경우 terminal node 표시
            return True # 현재 노드는 safe 

        for i in range(n):
            if isSafe(i):
                ans.append(i)
        
        return ans