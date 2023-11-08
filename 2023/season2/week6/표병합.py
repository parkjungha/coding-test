def solution(commands):
    answer = []
    merged = [[(i, j) for j in range(50)] for i in range(50)] # 각 셀의 병합 상태 배열
    board = [["EMPTY"] * 50 for _ in range(50)] # 각 셀의 문자열 값 저장

    for command in commands:
        command = command.split(' ')

        if command[0] == 'UPDATE': 
            if len(command) == 4: # 1. "UPDATE r c value"
                r, c, value = int(command[1])-1,int(command[2])-1,command[3]
                x, y = merged[r][c]
                board[x][y] = value

            elif len(command) == 3: # 2. "UPDATE value1 value2"
                value1, value2 = command[1], command[2]
                for i in range(50):
                    for j in range(50):
                        if board[i][j] == value1:
                            board[i][j] = value2

        elif command[0] == 'MERGE': # 3. "MERGE r1 c1 r2 c2"
            r1, c1, r2, c2 = int(command[1])-1, int(command[2])-1, int(command[3])-1, int(command[4])-1
            x1, y1 = merged[r1][c1]
            x2, y2 = merged[r2][c2]
            
            if board[x1][y1] == "EMPTY":
                board[x1][y1] = board[x2][y2]

            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x2,y2):
                        merged[i][j] = (x1,y1)

        elif command[0] == 'UNMERGE': # 4. "UNMERGE r c"
            r, c = int(command[1])-1,int(command[2])-1
            x, y = merged[r][c]
            tmp = board[x][y] # 병합을 해제하기 전 셀이 값을 가지고 있었을 경우
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x,y):
                        merged[i][j] = (i,j) # 병합 해제
                        board[i][j] = "EMPTY" # 초기 상태
            board[r][c] = tmp # 값 복원

        elif command[0] == 'PRINT':
            r, c = int(command[1])-1, int(command[2])-1
            x, y = merged[r][c]
            answer.append(board[x][y])
    return answer