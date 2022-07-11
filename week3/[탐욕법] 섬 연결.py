
# Kruskal 알고리즘
# 1) 최소 비용의 간선으로 구성됨 2) 사이클을 포함하지 않음 의 조건에 근거하여 각 단계에서 사이클을 이루지 않는 최소 비용 간선을 선택 한다.

def solution(n, costs):
    answer = 0
    connected = [costs[0][0]]
    costs = sorted(costs, key = lambda x: x[2]) # 최소 비용순으로 정렬  

    while len(connected) != n: # 모든 섬이 다 연결될때까지
        for i, cost in enumerate(costs):
            if cost[0] in connected and cost[1] in connected: # 이미 두노드가 다 연결되어 있다면
                continue
            if cost[0] in connected or cost[1] in connected: # 둘중 하나만 connection에 있을 경우 
                answer += cost[2]
                connected.append(cost[0])
                connected.append(cost[1])
                connected = list(set(connected)) # 중복 제거 
                costs.pop(i) 
                break 

    return answer