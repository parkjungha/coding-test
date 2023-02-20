# 맨해튼 거리는 |x1 - x2| + |y1 - y2| 
from collections import deque

def bfs(place): # 대기실 하나 
    people = []

    for row in range(5):
        for col in range(5):
            if place[row][col] == 'P':
                people.append([row,col])    
                
    # 상 하 좌 우 이동
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    
    for person in people: # 모든 사람에 대해서 검사하면서 거리두기 안지켰으면 바로 0
        q = deque([person]) # 시작점
        visited = [[0]*5 for _ in range(5)]
        dist = [[0]*5 for _ in range(5)]
        visited[person[0]][person[1]] = 1 # 시작노드 방문
        
        while q:
            y,x = q.popleft() # 현재 사람 위치

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                # 범위 안에 있고 방문하지 않았으면
                if 0 <= ny < 5 and 0 <= nx < 5 and visited[ny][nx] == 0:
                    if place[ny][nx] == 'O': # 빈 테이블이면 이동
                        q.append([ny,nx])
                        visited[ny][nx] = 1
                        dist[ny][nx] = dist[y][x] + 1

                    if place[ny][nx] == 'P' and dist[y][x] <= 1:
                        return 0
    return 1
    
def solution(places):
    answer = []

    for place in places:
        answer.append(bfs(place))

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
