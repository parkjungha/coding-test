class Solution:
    # DFS 
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:  
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for a,b in richer:
            graph[b].append(a)

        res = [-1] * n
        def dfs(node):
            if res[node] == -1:
                res[node] = node
                for rich in graph[node]: # 이웃 탐색
                    cand = dfs(rich) # 현재 res상에서 queitness 제일 작은 이웃 번호
                    if quiet[cand] < quiet[res[node]]: # 더 작은 quietness이면
                        res[node]  = cand # 더 작은 이웃으로 번호 업데이트
            return res[node]
        
        ans = []
        for i in range(n):
            ans.append(dfs(i))
        return ans