from collections import defaultdict

def solution(arrows):
    ans = 0
    visit = defaultdict(list) # 방문 체크
    x,y = 0,0
    dx = [0,1,1,1,0,-1,-1,-1]
    dy = [1,1,0,-1,-1,-1,0,1]

    # 방이 생기는 경우 
    # 1. 방문한 노드가 이미 방문한 적이 있고, 해당 노드로 들어온 경로는 처음 이동한 경우

    for i in arrows:
        for _ in range(2): # 노드가 없는 지점에서 대각선이 교차하는 경우를 처리하기 위해 한번에 2씩 이동
            nx = x + dx[i]
            ny = y + dy[i]  
            if (nx,ny) in visit and (x,y) not in visit[(nx,ny)]: # 방문했던 점이지만 경로가 겹치지 않는 경우, 방+1
                ans += 1
                visit[(x,y)].append((nx,ny))
                visit[(nx,ny)].append((x,y))

            elif (nx,ny) not in visit:  # 방문하지 않은 경우
                visit[(x,y)].append((nx,ny))  # 경로가 겹치는 경우는 따로 해줄 필요 없음
                visit[(nx,ny)].append((x,y))
            x,y = nx, ny # 이동
    return ans