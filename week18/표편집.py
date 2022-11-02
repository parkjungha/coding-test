def solution(n, k, cmd):
    answer = ['O']*n
    curr = k # 현재 인덱스 초기화
    table = {i:[i-1,i+1] for i in range(n)}
    table[0] = [None, 1]
    table[n-1] = [n-2, None]
    stack = []
    for c in cmd:
        if c[0] == "C": # 삭제
            answer[curr] = 'X'
            prev, next = table[curr]
            stack.append([prev, curr, next])
            if next == None: # 마지막 행이면 이전 행 선택
                curr = table[curr][0]
            else:
                curr = table[curr][1]
            if prev == None: # 첫 행이 삭제되면
                table[next][0] = None # 다음 행의 이전 포인터 업데이트
            elif next == None: # 마지막 행이 삭제되면
                table[prev][1] = None # 이전 행의 다음 포인터 업데이트
            else: # 중간에 끼인 행이 삭제되면
                table[prev][1] = next # 양옆 행의 포인터 업데이트
                table[next][0] = prev
        
        elif c[0] == "Z": # 복원
            prev, now, next = stack.pop()
            answer[now] = 'O'
            if prev == None: # 첫행이 복원되면
                table[next][0] = now # 기존 첫행의 이전 포인터 업데이트 
            elif next == None: # 막행이 복원되면
                table[prev][1] = now 
            else:
                table[prev][1] = now
                table[next][0] = now
            
        else: # 셀 커서 이동 
            d, x = c.split()
            x = int(x)
            if d == "D":
                for _ in range(x):
                    curr = table[curr][1] # 다음다음다음
            else:
                for _ in range(x):
                    curr = table[curr][0] # 이전이전이전
    return ''.join(answer)

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]	))