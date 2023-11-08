from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = ''
    # 남은 거리 탐색 자주 해주어야 하므로 함수로 빼주기
    def distance(x1, y1):
        return abs(x1 - (r-1)) + abs(y1-(c-1))

    # 남은 거리가 k보다 크거나, (최단 거리-k)가 홀수라면 도착 불가능
    if distance(x-1, y-1) > k or (distance(x-1, y-1) - k) % 2:
        return 'impossible'
    
    # 탐색 방향 사전순: d l r u
    direct = {(1,0):'d', (0,-1):'l', (0,1):'r', (-1,0):'u'}
    q = deque()
    q.append((x-1, y-1, 0, '')) # (x좌표, y좌표, 이동 횟수, 이동 경로)
    
    while q:
        sx, sy, cnt, route = q.popleft()
        
        # 도착했는데 남은 거리가 홀수라면 도착 불가능
        if (sx, sy) == (r-1, c-1) and (k - cnt) % 2:
            return 'impossible'
        
        elif (sx, sy) == (r-1, c-1) and cnt == k: # 도착
            return route
        
        for dx, dy in direct: # 한 칸 이동
            nx, ny = sx + dx, sy + dy
            if 0 <= nx < n and 0 <= ny < m:  # 격자 안

                # 남은 거리 + 현재까지 이동 거리가 k보다 크다면 이동 X
                if distance(nx, ny) + cnt + 1 > k: 
                    continue
                
                # 어차피 사전순서로 탐색하기 때문에 한 방향이 queue에 담기면 그다음부턴 볼 필요 없다
                q.append((nx, ny, cnt + 1, route + direct[(dx, dy)]))
                break

    return answer
