from collections import deque

def bfs(x,y,col): # 현재 좌표 (i,j)에서 같은 블록 그룹 찾기
    q = deque()
    q.append((x,y))
    block_cnt, rainbow_cnt = 1,0 # 초기화
    blocks, rainbows = [[x,y]], []
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and a[nx][ny] == col: # 일반 블록일 경우
                visited[nx][ny] = 1
                block_cnt += 1
                blocks.append([nx,ny])
                q.append((nx,ny))
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and a[nx][ny] == 0: # 무지개 블록일 경우
                visited[nx][ny] = 1
                rainbow_cnt += 1
                block_cnt += 1
                rainbows.append([nx,ny])
                q.append((nx,ny))
    
    for x,y in rainbows:
        visited[x][y] = 0 # 무지개블록은 방문해제
            
    # block_info = [블록크기, 무지개개수, 기준블록좌표]
    return [block_cnt, rainbow_cnt, blocks + rainbows]

# 제거된 블록은 -2로 표시
def remove(block):
    for x,y in block:
        a[x][y] = -2

def gravity(a):
    for i in range(N-2, -1, -1): # 밑에서 두번째 칸부터 첫번째 행까지 쭉 체크
        for j in range(N): 
            if a[i][j] > -1: # 검정색이 아니면 (무지개 또는 일반 블록)
                r = i # 현재 행 값
                while True:
                    if 0<=r+1<N and a[r+1][j] == -2: # 다음 행이 범위 안이면서 제거된 블록이면 아래로 내림
                        a[r+1][j] = a[r][j]
                        a[r][j] = -2
                        r += 1
                    else: # 범위를 벗어낫거나 값이 있으면 멈춤
                        break
def rotate(a):
    new_a = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_a[N-1-j][i] = a[i][j]
    return new_a

# Main
N, M = map(int, input().split())
a = []
for _ in range(N):
    a.append(list(map(int,input().split())))

score = 0

# 1. Autoplay
while True:
    # 블록 그룹 전부 다 찾기
    visited = [[0]*N for _ in range(N)] # 방문체크
    blocks = [] # 가능한 블록 그룹들을 넣을 리스트
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and a[i][j] > 0: # 방문하지 않은 일반 블록이면
                visited[i][j] = 1 # 방문처리
                block_info = bfs(i,j,a[i][j]) # 인접한 블록 찾기 (블록 좌표, 블록 색)
                if block_info[0] >= 2: # 블록 크기가 2보다 크면
                # block_info = [블록크기, 무지개개수, 블록좌표]
                    blocks.append(block_info) # 블록그룹에 추가
    blocks.sort(reverse=True) # 블록 크기순으로 정렬 (크기->무지개개수->행열) 미쳤다;;

    # 2. 가장 큰 그룹 제거하고 점수 계산
    if not blocks: # 블록 그룹이 더이상 없으면 중단
        break
    remove(blocks[0][2]) # 가장 큰 블록그룹 제거
    score += blocks[0][0]**2 # 가장 큰 블록그룹 크기**2

    # 3. 중력 4. 회전 5. 중력
    gravity(a)
    a = rotate(a)
    gravity(a)
    
print(score)
