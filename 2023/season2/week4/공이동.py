def solution(n, m, x, y, queries):
    # 모든 시작점 완전 탐색 -> O(n*m) 시간초과 (TC1만 됨...)

    def move_ball(sx,sy):
        for query in queries:
            cmd, dx = query
            if cmd == 0: # 열 감소
                sy -= dx
                if sy < 0: 
                    sy = 0

            elif cmd == 1: # 열 증가
                sy += dx
                if sy >= m:
                    sy = m-1

            elif cmd == 2: # 행 감소
                sx -= dx
                if sx < 0:
                    sx = 0

            elif cmd == 3: # 행 증가
                sx += dx
                if sx >= n:
                    sx = n-1
        
        return (sx == x) and (sy == y)


    for i in range(n):
        for j in range(m):
            if move_ball(i,j):
                cnt += 1
    
    return cnt
    
# 정답 칸에서 시작해서 쿼리를 역순으로 돌면서 가능한 시작점의 범위를 구해나가는 것
# 시작점의 범위를 구해서 해당 범위 내에 있는 모든 칸 Return -> O(n)

def solution(n, m, x, y, queries):
    x_min, x_max, y_min, y_max = x,x,y,y # 범위 초기화 (도착칸)
    for idx in range(len(queries)-1, -1, -1): # 쿼리 역순으로 순회
        cmd, dx = queries[idx]
        if cmd == 0: # 열 감소
            y_max += dx
            if y_max >= m: 
                y_max = m-1
            if y_min != 0: # 가장자리가 아닌 경우만
                y_min += dx

        elif cmd == 1: # 열 증가
            y_min -= dx
            if y_min < 0:
                y_min = 0
            if y_max != m-1:
                y_max -= dx
        
        elif cmd == 2: # 행 감소
            x_max += dx
            if x_max >= n:
                x_max = n-1
            if x_min != 0:
                x_min += dx

        else: # 행 증가
            x_min -= dx
            if x_min < 0:
                x_min = 0
            if x_max != n-1:
                x_max -= dx

        # 중간에 범위를 아예 벗어나서 결과가 0인 경우
        if y_min > m - 1 or y_max < 0 or x_min > n - 1 or x_max < 0:
            return 0
    
    # 범위 내에 있는 모든 점의 개수 반환
    return (y_max - y_min + 1) * (x_max - x_min + 1)