def solution(info, edges):
    visited = [0]*len(info) # i번째 노드 방문 체크
    visited[0] = 1 # root node부터 시작
    answer = []

    def dfs(sheep, wolf): # 양의 수, 늑대의 수
        if sheep > wolf:
            answer.append(sheep)

        else: # 늑대 수가 같거나 많아지면 내려가지 않음
            return

        # 아래로 탐색
        for i in range(len(edges)):
            parent = edges[i][0]
            child = edges[i][1]
            iswolf = info[child] # 내려갈 자식 노드가 늑대면 1, 아니면 0
            if visited[parent] and not visited[child]:
                visited[child] = 1
                if iswolf: # 늑대면
                    dfs(sheep, wolf+1)
                else: 
                    dfs(sheep+1, wolf)
                visited[child] = 0

    dfs(1,0)
    return max(answer)