from copy import deepcopy
import sys 

n, m = map(int, input().split())
cctv = []
array = []
mode = [
    [],
    [[0],[1],[2],[3]], # 1
    [[0,2],[1,3]], # 2
    [[0,1],[1,2],[2,3],[0,3]], # 3
    [[0,1,2],[0,1,3],[0,2,3],[1,2,3]], # 4
    [[0,1,2,3]] # 5
]
# 북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(n):
    a = list(map(int,input().split()))
    array.append(a)
    for j in range(m):
        if a[j] in [1,2,3,4,5]: # cctv면
            cctv.append([a[j], i,j]) # cctv종류와 좌표 정보 저장
        
def fill(board, dirs, x, y):
    for dir in dirs: # 해당하는 방향
        nx = x
        ny = y
        while True:
            nx += dx[dir]
            ny += dy[dir]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6: # 벽이면
                break
            elif board[nx][ny] == 0: # 빈칸이면
                board[nx][ny] = 7 # 감시당하는 영역 표시

def dfs(depth, arr):
    global minVal
    if depth == len(cctv): # 종료조건 
        count = 0
        for i in range(n):
            count += arr[i].count(0) # 사각지대 개수
        minVal = min(minVal, count)
        return 
    temp = deepcopy(arr)
    cctv_type, x, y = cctv[depth]
    for i in mode[cctv_type]:
        fill(temp,i,x,y)
        dfs(depth+1, temp)
        temp = deepcopy(arr) # 원상복구
    
minVal = sys.maxsize
dfs(0, array)
print(minVal)
