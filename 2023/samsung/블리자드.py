
# 중앙에서 시작해서 토네이도처럼 탐색을 진행
# 탐색하는 순서대로 맵에 표시 0부터 N**2 -1 까지 좌표를 기록

def make_orer_map():
    y = N//2
    x = N//2 # 중앙 idx
    order_pos.append((y,x))
    dy = [0,1,0,-1] # 왼 아래 오른 위
    dx = [-1,0,1,0]
    cd = 0 # 왼쪽부터
    step = 0 # 11 22 33 44
    while True:
        if cd % 2 == 0: # 왼 오른일때 step 증가
            step += 1
        flag = True
        for _ in range(step):
            y += dy[cd]
            x += dx[cd]
            order_pos.append((y,x))
            if x == 0 and y == 0:
                flag = False
                break
        if not flag:
            break
        cd = (cd+1)%4

def solve(board, m):
    if m == M: # M번 마법
        return 
    
    D,S = cmd[m][0], cmd[m][1] # 방향 거리
    cy = cx = N//2 # 상어 위치 중앙
    for s in range(1, S+1): # 1부터 S까지 d방향으로 구슬 없애줌
        ny = cy + (s*dx[D])
        nx = cx + (s*dy[D])
        if check_range(ny, nx):
            board[ny][nx] = 0
        
    # 빈칸 채우기
    move_to_empty(board)

    # 연속된 4개의 숫자 폭발시킴
    while find_4_numbers(board):
        move_to_empty(board) # 빈칸 채우기
    
    # 번호그룹으로 보드 재배열
    make_group(board)

    solve(board, m+1) # M번 반복

def move_to_empty(board):
    empty = deque() # 빈칸의 좌표
    for y,x in order_pos: # 탐색 순서대로 돌면서
        if board[y][x] == 0: # 빈칸이면
            empty.append((y,x))
        elif board[y][x] > 0 and empty: # 빈칸이 아닌데 앞에 빈칸이 있으면 옮겨줌
            ey, ex = empty.popleft()
            board[ey][ex] = board[y][x]
            board[y][x] = 0 # 해당 칸은 비워줌
            empty.append((y,x))

def find_4_numbers(board):
    visited = deque()
    cnt = 0
    number = -1
    flag = False
    for y,x, in order_pos:
        if y == N//2 and x == N//2: 
            continue
        if number == board[y][x]: # 연속된 숫자
            cnt += 1
            visited.append((y,x))
        else: # 다른 숫자 나오면
            if cnt >= 4: # 4개 이상이었다면
                flag = True
                scores[number] += count
            while visited:
                ny, nx = visited.popleft()
                if count >= 4:
                    board[ny][nx] = 0

            cnt = 1
            number = board[y][x]
            visited.append((y,x))
    return flag

def make_group(board):
    number = -1
    cnt = 0
    numbers = [0]
    for y,x in order_pos:
        if y == N//2 and X//2:
            continue
        if number == -1:
            number = board[y][x]
            cnt = 1
        else:
            if number == board[y][x]:
                cnt += 1
            else:
                numbers.append(cnt)
                numbers.append(number)
                cnt = 1
                number = board[y][x]

    idx = 0
    for y,x in order_pos:
        board[y][x] = numbers[idx]
        idx += 1
        if idx >= len(numbers):
            break