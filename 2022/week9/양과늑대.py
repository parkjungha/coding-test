# edges = [부모 노드, 자식 노드]
# 다른 칸으로 건너갈 수 있는 조건
   # 1. 부모 노드를 먼저 방문했는가?
   # 2. 자식 노드를 방문한 적이 없는가?

# 모을 수 있는 양은 최대 몇 마리인지 return

def solution(info, edges):
    visited = [0]*len(info) # 방문 여부
    visited[0] = 1 # 루트 노드부터 시작
    answer = []

    def dfs(sheep,wolf):
        if sheep > wolf: # 양이 더 많으면 이동한다
            answer.append(sheep)
        
        else: # 늑대가 더 많으면 가면 안됨
            return

        # 양이 더 많을 때.
        for i in range(len(edges)): # edges의 길이 = info의 길이 - 1
            parent = edges[i][0] 
            child = edges[i][1]
            iswolf = info[child] # 늑대면 1 양이면 0
            if visited[parent] and not visited[child]: # 부모 노드를 방문했고 자식 노드를 방문하지 않았다면
                visited[child] = 1 # 자식 방문
                dfs(sheep+(iswolf==0), wolf+(iswolf==1)) # 자식이 늑대인지 양인지에 따라 개수 업데이트 해서 재귀 
                visited[child] = 0

    dfs(1, 0) # 처음엔 루트 노드 양 한마리부터 시작
    return max(answer)