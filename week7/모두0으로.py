import sys
sys.setrecursionlimit(300000)
from collections import defaultdict

answer = 0
# Leaf 노드를 Call한 Parent 노드에게 가중치를 전달하면서 정답값에 더해준다

def dfs(x,a,tree,visited):
    global answer
    visited[x] = 1
    for y in tree[x]:
        if not visited[y]: # dfs로 방문하지 않은 leaf node까지 탐색 
            a[x] += dfs(y,a,tree,visited) # 자신을 dfs로 호출한 부모 정점에 자신의 가중치를 더함
    answer += abs(a[x]) # 현재 node를 0으로 만들기 위한 연산의 횟수는 node의 가중치의 절대값
    return a[x]

def solution(a, edges):
    global answer

    if sum(a) != 0: # 모든 점들의 가중치를 0으로 만드는 것이 불가능
        return -1

    tree = defaultdict(list)
    for i, j in edges:
        tree[i].append(j)
        tree[j].append(i)
        
    visited= [0]*len(a)
    dfs(0,a,tree,visited)
    
    return answer