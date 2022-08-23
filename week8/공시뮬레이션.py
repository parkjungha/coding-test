def solution(n, m, x, y, queries):
    answer = 0
    dy = [0,0,1,-1] # 행
    dx = [-1,1,0,0] # 열 

    # 모든 시작점에 대해서 query 수행해서 도착하는지 확인 O(n*m*q)
    for r in range(n): # 행
        for c in range(m): # 열
            curR, curC = r,c # 시작점
            for com,dist in queries: # 쿼리 다 수행

                # 이동
                curR += dy[com]*dist
                curC += dx[com]*dist
                
                # 범위에서 벗어난 경우 처리
                if curC < 0: curC = 0
                elif curC > m-1: curC = m-1
                if curR < 0: curR = 0
                elif curR > n-1: curR = n-1

            # 쿼리 끝났을 때 시작점에 도착했으면 
            if curR == x and curC == y:
                answer += 1
    return answer

print(solution(2,2,0,0,[[2,1],[0,1],[1,1],[0,1],[2,1]]))

print(solution(2,5,0,1,[[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]))

def solution(n, m, x, y, queries):
    answer = 0
    x_min, x_max, y_min, y_max = x,x,y,y

    for idx in range(len(queries)-1, -1, -1): # query 역순으로 순회
        dir, dist = queries[idx]

        # 열 번호가 감소하는 방향
        if dir == 0: 
            y_max += dist # 열 번호 증가
            if y_max > m-1: # 범위 벗어나면
                y_max = m-1
            if y_min != 0: # 왼쪽 값이 끝이 아니면 
                y_min += dist # 범위 축소

        # 열 번호가 증가하는 방향
        elif dir == 1:
            y_min -= dist
            if y_min < 0:
                y_min = 0
            if y_max != m-1:
                y_max -= dist

        # 행 번호가 감소하는 방향
        elif dir == 2:
            x_max += dist
            if x_max > n-1:
                x_max = n-1
            if x_min != 0:
                x_min += dist
        
        # 행 번호가 증가하는 방향
        else:
            x_min -= dist
            if x_min < 0:
                x_min = 0
            if x_max != n-1:
                x_max -= dist
        
        if y_min > m-1 or y_max < 0 or x_min > n-1 or x_max < 0:
            return answer
        
    else:
        answer = (y_max - y_min + 1) * (x_max - x_min + 1)
    return answer