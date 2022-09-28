from collections import deque, defaultdict

def solution(n, wires):
    answer = 100000
    graph = defaultdict(list)
    for wire in wires: # 양방향 그래프 연결 정보 저장
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])

    for wire in wires:
        v1 = wire[0]
        v2 = wire[1]
        diff = abs(bfs(v1, v2, wires, n, graph) - bfs(v2, v1, wires, n, graph))
        answer = min(diff, answer) # 두 전력망이 가지고 있는 송전탑 개수의 차이의 최솟값
    
    return answer # 연결된 송전탑 수 

def bfs(start, cut, wires, n, graph):
    cnt = 0
    visited = [0]*(n+1)
    q = deque([start])
    visited[start] = 1

    while q:
        curr = q.popleft()
        for next in graph[curr]: # 현재 노드와 연결된 노드들 
            if next == cut: continue # 끊어진 송전탑
            if visited[next] == 1: continue # 이미 방문하였다면
            cnt += 1
            q.append(next)
            visited[next] = 1

    return cnt