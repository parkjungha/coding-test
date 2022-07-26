from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)

    for ticket in tickets:
        routes[ticket[0]].append(ticket[1]) # 출발지: [도착지] 사전 만들기

    for key in routes.keys():
        routes[key].sort(reverse=True) # 도착지 알파벳 순 정렬 (pop으로 빼야하니까 역순)

    stack = ["ICN"]
    while stack: # stack이 빌때까지
        tmp = stack[-1]

        if not routes[tmp]: # 현재 지점을 시작점으로 하는 노선이 없는 경우
            answer.append(stack.pop())
        else: # 있는 경우
            stack.append(routes[tmp].pop()) # 알파벳순으로 선택
    
    return answer[::-1] # 거꾸로