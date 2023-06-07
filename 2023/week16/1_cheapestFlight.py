class Solution:
    # Dijkstra algorithm with at most k stops
    # 우선순위 큐로 최소 비용 가져오기
    # Runtime 40.29% (220ms) Memory 6.38% (19.2MB)
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        G = defaultdict(list)
        for v, w, d in flights: # from, to, price
            G[v].append((w,d))
        heap = [(0, 0, src)] # (비용, stop 횟수, 노드 번호)
        visited = set() # 방문 기록

        while heap: # heapq가 빌때까지
            d, curk, v = heappop(heap) # 최소 비용으로 갈 수 있는 노드가 뽑힘 

            if v == dst: # 목적지 노드 도착 -> 최소비용 반환
                return d

            if (v, curk) in visited or curk > k: # 이미 방문했거나, 최대 방문할 수 있는 횟수 지나면, 넘어감
                continue
            visited.add((v, curk)) # 방문하지 않은 경우 기록

            for w, ecost in G[v]: # 현재 노드에 연결된 이웃 노드들 heapq에 담음 -> 최소 비용순으로 자동 정렬됨
                heappush(heap, (d+ecost, curk+1, w))
        
        return -1 # heapq가 빌때까지 목적지에 도착하지 못하면 -1 반환
            