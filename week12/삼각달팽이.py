# 숫자가 1씩 증가하면서 끝변까지 다다르면 방향 전환

def solution(n):
    answer = []
    array = [[0]*n for _ in range(n)] # 2차원 Arr
    x,y = -1, 0
    num = 1

    for i in range(n):
        for _ in range(i,n):
            if i % 3 == 0: # 아래
                x += 1
            elif i % 3 == 1: # 오른쪽
                y += 1
            elif i % 3 == 2: # 위쪽
                x -= 1
                y -= 1
            array[x][y] = num
            num += 1
    
    for i in array:
        for j in i:
            if j:
                answer.append(j)
    
    return answer