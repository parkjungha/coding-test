class Solution:
    # Runtime 325ms (89.11%) / Memory 17.91mb (85.85%)
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for i in range(n)]

        for r in roads:
            u,v = min(r), max(r) # 정렬해서 작은거 u, 큰거 v
            graph[u].append(v)
            graph[v].append(u)

        ans = 0
        for i in range(n):
            for j in range(i+1, n): 
                if i != j: # 모든 pair에 대해서 확인 
                    cnt = len(graph[i]) + len(graph[j])
                    if j in graph[i]: # 두 도시를 서로 연결한다면 하나로 cnt 
                        cnt -= 1
                    ans = max(ans, cnt) # max 값 갱신

        return ans