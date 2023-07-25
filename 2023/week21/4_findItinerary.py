import collections
import heapq

class Solution:
    # DFS 탐색 + min heap 사용
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ans = []
        graph = collections.defaultdict(list)

        for a, b in tickets:
            graph[a].append(b) # a는 source, b는 destination 

        for u in graph: # for each source node
            heapq.heapify(graph[u]) # minheap -> sort destinations by lexical order 

        def dfs(u: str) -> None:
            while u in graph and graph[u]:
                dfs(heapq.heappop(graph[u])) # pop smallest destination -> 재귀적으로 시작 노드가 되서 DFS 탐섹
            ans.append(u) # 맨 마지막 destination node부터 쌓임

        dfs('JFK') # 부터 시작
        return ans[::-1] # 뒤집어서 반환