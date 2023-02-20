
def dfs(queen, row, n):
    # queen 배열은 index가 row, 값이 col
    cnt = 0
    if n == row: # 끝까지 도달
        return 1

    # 퀸을 놓을 수 있는지 확인
    for col in range(n): # 행 하나씩 배치
        queen[row] = col
        for i in range(row):
            if queen[i] == queen[row]: # 세로로 겹치면
                break
            if abs(queen[i]-queen[row]) == row -i: # 대각선으로 겹치면
                break
        
        else: # 겹치지 않는다면 다음 진행
            cnt += dfs(queen, row+1, n)
        
    return cnt

def solution(n):
    return dfs([0]*n, 0, n)