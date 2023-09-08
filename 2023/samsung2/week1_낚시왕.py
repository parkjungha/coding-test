
r,c,m = map(int, input().split())

sharks = []
for _ in range(m): # 상어의 정보
    sharks.append(list(map(int, input().split())))
    # (r,c), s, d, z 
    # 위치x y , 속력, 이동방향, 크기
    # d = 상 하 우 좌 1 2 3 4

array = [[0 for _ in range(c+1)] for _ in range(r+1)]

# 격자에 상어 배치
for shark in sharks:
    array[shark[0]][shark[1]] = [shark[2],shark[3],shark[4]] # (속력, 이동방향, 크기)

def move():
    dx = [0,-1,1,0,0]
    dy = [0,0,0,1,-1]
    for x in range(1, r+1):
        for y in range(1, c+1):
            if array[x][y]: # 현재 칸에 상어가 있으면
                s, d, z = array[x][y] # 속력, 이동방향, 크기
                move = 0
                if d <= 2: # 상 하
                    s %= (r-1)*2
                else: 
                    s %= (c-1)*2
                while move < s:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx<0 or nx>=r or ny<0 or ny>=c:
                        nx -= dx[d]
                        ny -= dy[d]
                        if d == 1:
                            d = 2
                        elif d == 2:
                            d = 1
                        elif d == 3:
                            d = 4
                        elif d == 4:
                            d = 3
                        nx += dx[d]
                        ny += dy[d]
                    move += 1
                        
#####################################################################
                if not array[nx][ny]: # 이동할 칸이 빈칸이면
                    array[nx][ny] = array[x][y] # 상어 이동

                elif array[nx][ny][2] < array[x][y][2]: # 새로운상어가 더 큰 경우
                    array[nx][ny] = array[x][y] # 상어 이동
                array[x][y] = 0


ans = 0 # 낚시왕이 잡은 상어 크기의 합
for cc in range(1, c+1): # 낚시왕이 첫번째 열부터 마지막 열까지 이동
    print("@@@", cc, "초 @@@")
    # 1.낚시왕이 오른쪽으로 한 칸 이동한다.
    # 2.낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 
    for rr in range(1, r+1):
        if array[rr][cc]: 
            ans += array[rr][cc][2] 
            print("잡은 상어 크기",array[rr][cc][2])
            array[rr][cc] = 0 # 상어가 사라진다.

    move() # 3. 상어가 이동한다. 
    print("상어 이동 완료")
    print(array)

print(ans)