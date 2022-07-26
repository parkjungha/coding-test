from collections import deque
'''
매개변수: 
# 지형을 나타내는 직사각형이 담긴 2차원 배열 rectangle
# 초기 캐릭터의 위치 characterX, characterY 
# 아이템의 위치 itemX, itemY

Return:
캐릭터가 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리
'''

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    board = [[0]*101 for _ in range(101)] # 모든 좌표 두배 해주기
    cX = characterX * 2
    cY = characterY * 2
    iX = itemX * 2
    iY = itemY * 2
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    visited = [[0]*101 for _ in range(101)]
    visited[cX][cY] = 1
    queue = deque([(cX, cY)])

    # 직사각형 (테두리와 내부) 1로 표시
    for x1, y1, x2, y2 in rectangle:
        for x in range(2*x1, 2*x2+1):
            for y in range(2*y1, 2*y2+1):
                board[x][y] = 1

    # 다시 내부 0으로 표시 -> 한 직사각형의 테두리가 다른 직사각형의 내부라면 0 처리
    for x1, y1, x2, y2 in rectangle:
        for x in range(2*x1+1, 2*x2):
            for y in range(2*y1+1, 2*y2):
                board[x][y] = 0

    while queue:
        x,y = queue.popleft()
        if (x,y) == (iX, iY): # 아이템 위치에 도착
            answer = (board[x][y]-1) // 2 # 최단거리 반환 (1을 빼는 이유는 board[cX][cY] = 1 로 시작했기 때문)
            break

        for i in range(4): 
            xTemp = x+dx[i]
            yTemp = y+dy[i]

            if 0 <= xTemp < 101 and 0 <= yTemp < 101 and board[xTemp][yTemp] != 0 and visited[xTemp][yTemp] == 0:
                board[xTemp][yTemp] = board[x][y] + 1
                visited[xTemp][yTemp] = 1
                queue.append((xTemp, yTemp))

    return answer 

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))