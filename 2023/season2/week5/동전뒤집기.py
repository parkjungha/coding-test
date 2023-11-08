'''
def solution(beginning, target):
    n = len(beginning)
    m = len(beginning[0])

    isSame = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(beginning[i][j] == target[i][j])
        isSame.append(row)
    # [[True, False, True, False, False], [False, True, False, True, True], [True, False, True, False, False], [False, True, False, True, True], [True, False, True, False, False]]

    first = board[0]
    cnt = first.count(False)
    print(first)

    for i in range(1, n):
        if isSame[i] != first:
            for j in range(m):
                if first[j] == isSame[i][j]:
                    return -1
            cnt += 1
    
    return min(cnt, n+m-cnt)

'''
# https://codingbutterfly.tistory.com/62
def solution(beginning, target):

    def flipRow(row):
        for j in range(m):
            beginning[row][j] = not beginning[row][j]

    def compareColumn(col):
        cnt = 0
        for i in range(n):
            if beginning[i][col] == target[i][col]:
                cnt += 1
        
        if cnt == 0: return 1 # 현재 열에서 모든 값이 전부 반대인 경우
        if cnt == n: return 0 # 현재 열에서 모든 값이 전부 동일한 경우
        else: return -1 

    def dfs(row, cnt, answer):
        print((row, cnt, answer))
        # 모든 행에서 뒤집거나 뒤집지 않은 선택을 완료한 경우
        if row == n:
            flag = True
            # 각 열의 상태를 비교하여 target과 동일하게 만들 수 있는지 판별
            for j in range(m):
                currCol = compareColumn(j)
                if currCol == -1: # 현재 상태에서 target과 동일하게 만들 수 없다면
                    flag = False
                    break
                cnt += currCol

            if flag:
                answer = min(answer, cnt) # target과 동일하게 만들 수 있는 경우 최소 횟수 갱신
                return answer

        else: # row != n
            dfs(row + 1, cnt, answer) # 현재 행 뒤집지 않을 때
            flipRow(row)
            dfs(row + 1, cnt + 1, answer) # 현재 행 뒤집었을 때
            flipRow(row) # 원상 복구

    answer = float("inf")
    n = len(beginning)
    m = len(beginning[0])

    answer = dfs(0, 0, answer)
    
    if answer == float('inf'):
        return -1

    return answer

beginning = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]	
target = [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]	

print(solution(beginning, target))