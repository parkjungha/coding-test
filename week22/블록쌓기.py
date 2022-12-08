# 각 블럭마다 비어있는 공간 찾기
def check_diff(lst):
    row = set()
    col = set()
    for r,c in lst:
        if r not in row:
            row.add(r)
        if c not in col:
            col.add(c)
    answer = []
    for r in row:
        for c in col:
            if (r,c) not in lst:
                answer.append((r,c))
    return answer

# 제거할 수 있는지 체크
def can_del(lst, black):
    for block in lst:
    # 각 블럭에서 비어있는 부분과, 검정 블록이 들어갈 수 있는 위치 비교해서 일치하면 채워서 제거함
        if block not in black: 
            return False
    return True

def solution(board):
    N = len(board)
    answer = 0
    updated = True
    while updated:
        block_info = {}
        black = set() # 검정 블록을 쌓을 수 있는 위치
        check = [0 for _ in range(N)]
        for i in range(N):
            for j in range(N):
                typed = board[i][j]
                if typed != 0:
                    if typed in block_info:
                        block_info[typed][0].append((i,j)) # 각 블럭이 채워져있는 부분 [0]
                    else:
                        block_info[typed] = [[(i,j)],list()]
                    check[j] = 1
                else:
                    if not check[j]:
                        black.add((i,j))
        for typed in block_info:
            block_info[typed][1] = check_diff(block_info[typed][0]) # 각 블럭에서 비어있는 공간 [1]

        updated = False
        for typed in block_info:
            if can_del(block_info[typed][1],black):
                # 삭제 가능
                answer += 1
                updated = True
                for i,j in (block_info[typed][0] + block_info[typed][1]):
                    board[i][j] = 0
                # 제거해서 해당 타입의 블록 0으로 만들고 다시 전체 루프 반복
                
    return answer