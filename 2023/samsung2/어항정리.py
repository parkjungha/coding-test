
# 물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다. 
def fillFish(fishes):
    minVal = min(fishes)
    for i in range(len(fishes)):
        if fishes[i] == minVal:
            fishes[i] += 1
    return fishes

def stackFirst(fishes): # fishes는 1차원 list
    bowl = fishes[:]  # 1차원인 부분 [5 3 3 14 9 3 11 8]
    stack = [[bowl[0]], [bowl[1]]]  # [[5], [3]]
    bowl = bowl[2:] # [3 14 9 3 11 8]

    while True:
        height = len(stack) # 2 / 2
        width = len(stack[0]) # 1 / 2

        if len(bowl) >= height: # 일때 회전 가능
            # stack 2차원 배열 회전 
            temp = [[0]*height for _ in range(width)] 
            for i in range(width):
                for j in range(height):
                    temp[i][j] = stack[height-j-1][i] # Matrix 90도 회전 공식
                    # [[3,5]] / [[3,3],[14,5]]
                    
            # 위에 쌓기
            stack = temp + [bowl[:height]] # [[3,5], [3,14]] / [[3,3],[14,5], [9,3]]
            bowl = bowl[height:] # [9,3,11,8] / [11,8]
            
        else: # 회전 불가능 # [9,3, 11,8]
            stack[-1] = stack[-1] + bowl # 마지막에 1차원인 부분 붙여줌
            break
            # [[3,3],[14,5], [9,3,11,8]]

    # 최대 길이(맨아래줄) 에 맞춰서 -1 붙여줌
    for i in range(len(stack)-1): # 맨 아래줄 빼고
        stack[i].extend([-1]*(len(stack[-1])-len(stack[i])))
        # [[3,3,-1,-1], [14,5,-1,-1], [9,3,11,8]]

    # 공중 부양시킨 어항 중 가장 오른쪽에 있는 어항의 아래에 바닥에 있는 어항이 있을때까지 
    # Return: fish_mat: 2차원 list 
    return stack

from copy import deepcopy

def adjustFish(fish_mat):
# 모든 인접한 두 어항에 대해서, 물고기 수의 차이를 구한다. 
# 이 차이를 5로 나눈 몫을 d라고 하자. 
# d가 0보다 크면, 두 어항 중 물고기의 수가 많은 곳에 있는 물고기 d 마리를 적은 곳에 있는 곳으로 보낸다. 
# 이 과정은 모든 인접한 칸에 대해서 동시에 발생한다.
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    width = len(fish_mat[0])
    height = len(fish_mat)
    # 모든 점 (-1이 아닌)이 시작점
    visited = [[0]*width for _ in range(height)]

    temp = deepcopy(fish_mat) # 원본 보존 용도
    for x in range(height):
        for y in range(width):
            visited[x][y] = 1
            if fish_mat[x][y] != -1:
                for i in range(4): # 현재 칸에서 인접한 네칸 방문
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if 0<=nx<height and 0<=ny<width and visited[nx][ny]==0 and fish_mat[nx][ny] != -1:
                        diff = fish_mat[nx][ny] - fish_mat[x][y]
                        d = abs(diff)//5
                        if d > 0:
                            if diff > 0:
                                temp[nx][ny] -= d
                                temp[x][y] += d
                            else:
                                temp[nx][ny] += d
                                temp[x][y] -= d
    return temp
                        

# 어항을 바닥에 일렬로 놓기.
def flatten(fish_mat):
    fish_1d = []
    for i in range(len(fish_mat[0])): # 가장 왼쪽에 있는 어항부터
        for j in range(len(fish_mat)-1, -1, -1): # 아래부터 위로
            if fish_mat[j][i] != -1:
                fish_1d.append(fish_mat[j][i])
    return fish_1d

# print(ans)

def stackSecond(fishes): # fishes는 1차원 list
# 가운데를 중심으로 왼쪽 N/2개를 공중 부양시켜 
# 전체를 시계 방향으로 180도 회전 시킨 다음, 
# 오른쪽 N/2개의 위에 놓아야 한다.
# 두 번 반복
    N = len(fishes)
    left = fishes[:N//2]
    left = left[::-1]
    right = fishes[N//2:]
    stack = [left, right]
    # 5 5 10 9
    # 6 3 10 8

    swipe = [[],[]] # 1행, 2행
    right = [[],[]]
    
    for r in range(2): # 2행
        for c in range(N//2): # N//4보다 작거나 같은 열
            if c < N//4:
                swipe[r].append(stack[r][c])
            else:
                right[r].append(stack[r][c])

    swipe[1], swipe[0] = swipe[0][::-1], swipe[1][::-1]

    return swipe + right


N, K = map(int, input().split())
fishes = list(map(int, input().split()))
ans = 0

while max(fishes) - min(fishes) > K:
    ans += 1
    fishes = flatten(adjustFish(stackFirst(fillFish(fishes)))) # 첫번째 공중부양
    fishes = flatten(adjustFish(stackSecond(fishes))) # 물고기수 조절

print(ans)
