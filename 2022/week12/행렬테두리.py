def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for i in range(columns+1)] for j in range(rows+1)]
    num = 1
    for row in range(1, rows+1):
        for column in range(1, columns+1):
            matrix[row][column] = num
            num += 1
            
    for x1, y1, x2, y2 in queries:
        tmp = matrix[x1][y1]
        mini = tmp
        
        for k in range(x1,x2): # y1 열 위로 올려줌
            matrix[k][y1] = matrix[k+1][y1]
            mini = min(mini, matrix[k][y1])

        for k in range(y1,y2): # x2 행 왼쪽 이동
            matrix[x2][k] = matrix[x2][k+1]
            mini = min(mini, matrix[x2][k])

        for k in range(x2,x1,-1): # y2 열 아래로 이동
            matrix[k][y2] = matrix[k-1][y2]
            mini = min(mini, matrix[k][y2])

        for k in range(y2,y1,-1): # x1 행 오른쪽 이동
            matrix[x1][k] = matrix[x1][k-1]
            mini = min(mini, matrix[x1][k])

        matrix[x1][y1+1] = tmp
        answer.append(mini)
            
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))