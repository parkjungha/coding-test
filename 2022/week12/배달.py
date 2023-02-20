# 1번 마을에 있는 음식점이 K 이하의 시간에 배달이 가능한 마을의 개수를 return 
# 최단거리 -> 다익스트라 알고리즘 : 특정 하나의 정점에서 다른 모든 정점으로 가는 최단 경로. 음의 간선 X 

import heapq

def dijkstra(dist,adj):
    # 출발 노드를 기준으로 각 노드들의 최소 비용 탐색
    heap = []
    heapq.heappush(heap, [0,1]) # 출발 노드 설정
    while heap:
        cost, node = heapq.heappop(heap) # 출발 노드를 기준으로 각 노드의 최소 비용 저장 
        for c,n in adj[node]: 
            if cost+c < dist[n]:
                dist[n] = cost+c
                heapq.heappush(heap, [cost+c,n])
    
def solution(N, road, K):
    dist = [float('inf')]*(N+1) # 1번 마을로부터 최소거리 갱신
    dist[1] = 0 # 본인
    adj = [[] for _ in range(N+1)] # 인접노드, 거리 기록
    for r in road: # 쌍방향
        adj[r[0]].append([r[2],r[1]])
        adj[r[1]].append([r[2],r[0]])
    dijkstra(dist, adj)

    return len([i for i in dist if i<= K])
