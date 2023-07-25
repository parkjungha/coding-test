class Solution:
    # 886. Possible Bipartition 문제와 완전 동일
    # BFS 탐색 - Queue 사용
    # Return a graph is bipartite or not.
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        groups = [0] * n # 아직 방문되지 않으면 0, 또는 그룹 number 1 또는 2 저장
        for i in range(n):
            if groups[i] == 0: # 아직 방문되지 않은 경우
                groups[i] = 1 # 방문 표시 
                q = deque([i]) # 시작노드 i 부터
                while q: # bfs 탐색
                    a = q.popleft() # 해당 노드 a의 
                    for b in graph[a]: # 이웃 노드 b 들
                        if groups[b] == 0: # 아직 이웃노드 b가 방문되지 않은 경우
                            groups[b] = 1 if groups[a] == 2 else 2 # a랑 반대 그룹 할당 (a가 1이면 b는 2, 2이면 1)
                            q.append(b)
                        elif groups[a] == groups[b]:
                            return False
        return True