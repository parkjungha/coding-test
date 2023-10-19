from copy import deepcopy

dir = [[0,1], [0,-1], [1,0], [-1,0]] # 4 방향 움직임

def canMove(board, loc):
    r,c = loc
    for idx, (dr, dc) in enumerate(dir): 
        nr = r + dr
        nc = c + dc
        if (0 <= nr < len(board)) and (0 <= nc < len(board[0])) and board[nr][nc] == 1: 
            return True
    return False

def search(board, aloc, bloc, step):
    if step % 2 == 0:
        r,c = aloc
    else: r,c = bloc

    if canMove(board, [r,c]) == False:
        return (False, 0) # 움직일 수 없는 경우
    if aloc == bloc: 
        return (True, 1) # 같은 위치에 있는 경우

    nboard = deepcopy(board)
    nboard[r][c] = 0 # 현재 위치
    canWin = False
    maxTurn, minTurn = 0, float('inf') # 최대 최소값 초기화
    for idx, (dr,dc) in enumerate(dir):
        nr = r + dr
        nc = c + dc
        if (0 <= nr < len(board)) and (0 <= nc < len(board[0])) and nboard[nr][nc] == 1: 
            # 이동하려는 칸이 범위 내에 있고, 발판이 존재할 때 (이동할 수 있는 칸일때)
            if step % 2 == 0: # a 차례
                ret = search(nboard, [nr, nc], bloc, step+1)
            else: # b c차례
                ret = search(nboard, aloc, [nr, nc], step+1)

            if ret[0] == False: 
                canWin = True
                minTurn = min(minTurn, ret[1])
            else:
                maxTurn = max(maxTurn, ret[1])

    if canWin == True: # 이기는 경우
        return (canWin, minTurn + 1) # 최소 움직임 반환
    else:
        return (canWin, maxTurn + 1) # 최대 움직임 반환

def solution(board, aloc, bloc):
    answer = search(board, aloc, bloc, 0)
    return answer[1]

print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1,0], [1,2]))