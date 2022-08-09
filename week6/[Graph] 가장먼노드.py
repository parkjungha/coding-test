from collections import deque # BFS

def solution(n, edge):
    answer = 0
    graph = [[]* n for _ in range(n+1)] # 각 노드와 연결된 노드표시
    for a,b in edge:
        graph[a].append(b) # 양방향
        graph[b].append(a) # 그래프
    
    visited = [0]*(n+1)
    visited[1] = 1 # 시작노드 1번
    queue = deque([1])

    while(queue):
        n = queue.popleft()
       
        for i in graph[n]: # 인접한 노드들에 대해서 모두 반복
            if visited[i] == 0: # 아직 방문하지 않은 노드이면
                queue.append(i) # 큐에 넣기 
                visited[i] = visited[n]+1 # 거리 카운트를 위해서 이전 노드 방문 수에서 ++1
                
    answer = visited.count(max(visited))
    return answer