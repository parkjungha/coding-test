# 효율성 X 시간복잡도 O(n*m)
def solution(board, skill):
    answer = 0
    for type, r1, c1, r2, c2, degree in skill:
        for y in range(r1, r2+1):
            for x in range(c1, c2+1):
                if type == 1:
                    board[y][x] -= degree
                elif type == 2:
                    board[y][x] += degree

    for y in board:
        for x in y:
            if x > 0:
                answer += 1
    
    return answer


# 효율성 -> 2차원 누적합 O(1)
# Range(x1, y1, x2, y2) = S(x2, y2) - S(x1, y2) - S(x2, y1) + S(x1, y1)
# 즉 (x1, y1) ~ (x2, y2)까지에 n만큼의 변화를 주고 싶다면,
# (x1, y1) = n, (x2+1, y1) = -n, (x1, y2+1) = -n, (x2+1, y2+1) = n 만큼의 값을 더해준다.
# 그 후 행, 열 누적합 진행 후, 배열을 기존 board배열에 더해준다.

def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    tmp = [[0]*(m+1) for _ in range(n+1)]

    for type, r1, c1, r2, c2, degree in skill:
        tmp[r1][c1] += degree if type ==2 else -degree
        tmp[r1][c2+1] -= degree if type == 2 else -degree
        tmp[r2+1][c1] -= degree if type == 2 else -degree
        tmp[r2+1][c2+1] += degree if type==2 else -degree

    #행 기준 누적합
    for i in range(n):
        for j in range(m):
            tmp[i][j+1] += tmp[i][j]

    #열 기준 누적합
    for j in range(m):
        for i in range(n):
            tmp[i+1][j] += tmp[i][j]

    #기존 배열과 합함
    for i in range(n):
        for j in range(m):
            board[i][j] += tmp[i][j]
            # board에 값이 1이상인 경우 answer++
            if board[i][j] > 0: answer += 1
    return answer
