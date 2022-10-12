from collections import deque 
# ShiftRow는 각각의 행의 인덱스만 조정
# Rotate는 바깥쪽 열 2줄과 행 2줄의 원소들 각각 1개씩만을 옮기기
def solution(rc, operations):
    r_len, c_len = len(rc), len(rc[0])

    # ShiftRow 연산을 위해 행 별로 관리 (양쪽 원소 제외)
    rows = deque(deque(row[1:-1]) for row in rc)
    # Rotate 연산을 위해 양쪽 끝 열 별로 관리
    out_cols = [deque(rc[r][0] for r in range(r_len)), # 첫번째 열 값
                deque(rc[r][c_len - 1] for r in range(r_len))] # 마지막 열 값
    
    # 연산
    for operation in operations:
        if operation[0] == "S":
            # 마지막 행을 처음으로 이동
            rows.appendleft(rows.pop())
            # 첫번째 열과 마지막 열의 가장 아래 원소를 가장 위로 이동
            out_cols[0].appendleft(out_cols[0].pop()) # 첫번째 열
            out_cols[1].appendleft(out_cols[1].pop()) # 마지막 열

        else: # Rotate 연산
            # 마지막 열의 가장 아래 원소를 마지막 행의 가장 오른쪽으로 이동
            rows[r_len-1].append(out_cols[1].pop())
            # 마지막 행의 가장 왼쪽 원소를 첫번째 열의 가장 아래로 이동
            out_cols[0].append(rows[r_len-1].popleft())
            # 첫번째 열의 가장 위쪽 원소를 첫번째 행의 가장 왼쪽으로 이동
            rows[0].appendleft(out_cols[0].popleft())
            # 첫번째 행의 가장 오른쪽 원소를 마지막 열의 가장 위쪽으로 이동
            out_cols[1].appendleft(rows[0].pop())

    answer = []
    for r in range(r_len):
        answer.append([])
        answer[r].append(out_cols[0][r]) # 첫번째 열 값 삽입
        answer[r].extend(rows[r]) # 행 값들 삽입 (여러개 원소 한번에 리스트에 넣어야해서 extend)
        answer[r].append(out_cols[1][r]) # 마지막 열 값 삽입

    return answer

solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]]	, ["Rotate", "ShiftRow", "ShiftRow"]	)