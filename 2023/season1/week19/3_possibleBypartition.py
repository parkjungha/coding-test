
class Solution:
    # BFS -> Queue 
    # Runtime 86.44% (708ms) Memory 90.13% (21.8MB)
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # 서로 싫어하는 사람들 끼리 다른 그룹이 되도록 2개의 그룹으로 나눌 수 있는지 반환
        graph = [[] for _ in range(n)]
        for a, b in dislikes:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)

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