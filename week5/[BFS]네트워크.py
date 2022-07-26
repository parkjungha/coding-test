# 전체 노드들에 대해서, 방문하지 않은 노드들에 대해서 다 돌면서 체크

def solution(n, computers): # n은 node의 개수, computers는 Adjacency Matrix 
    answer = 0
    visit = [0 for _ in range(n)] # 방문 표시
    for com in range(n): 
        if visit[com] == 0:
            BFS(n, computers, com, visit)
            DFS(n, computers, com, visit)
            answer += 1
    return answer

# BFS : Queue로 구현
def BFS(n, computers, com, visit):
    visit[com] = 1 # 해당 노드 방문 표시
    queue = []
    queue.append(com)
    while queue: # 방문되지 않은 노드가 없을때까지 반복 
        com = queue.pop(0)
        visit[com] = 1
        for i in range(n):
            if computers[com][i] == 1 and visit[i] == 0: # 해당 노드와 연결되어 있고, 아직 방문하지 않은 노드이면 
                queue.append(i) 

# DFS : Recursion으로 구현.
def DFS(n, computers, com, visit):
    visit[com] = 1 # 해당 노드 방문 표시
    for i in range(n):
        if computers[com][i] == 1 and visit[i] == 0: 
            dfs(n, computers, i, visit) # 재귀 
 
