class Solution: 
    # 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야하는 경우 -> 플로이드 워셜 알고리즘
    # 한 지점에서 다른 특정 지점까지의 최단 경로를 구하는 경우 -> 다익스트라 알고리즘

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float("inf") for i in range(n)]for i in range(n)] 
        # 2차원 배열에 거리 정보 저장 
        for src,dst,w in edges:
            dist[src][dst] = w
            dist[dst][src] = w
        for i in range(n): # self-edge dist = 0 
            dist[i][i] = 0

        # Floyd Warshall Algorithm 
        for k in range(n): # 거쳐가는 노드 k
            for i in range(n): # 출발 노드 i
                for j in range(n): # 도착 노드 j  
                    if dist[i][k] == float("inf") or dist[k][j] == float("inf"): # k를 거쳐갈 수 없는 경우 
                        continue
                    dist[i][j] = min(dist[i][j],(dist[i][k]+dist[k][j])) 

        # 각 노드의 Reachable city within threshold 개수 count
        minCnt = n
        ans = 0
        for city in range(n):
            #  counter for every city
            cnt = 0
            for adj in range(n):
                if city == adj: # 본인 번호
                    continue
                if dist[city][adj] <= distanceThreshold:
                    cnt += 1
            if cnt <= minCnt: 
                minCnt = cnt
                ans = city
        return ans