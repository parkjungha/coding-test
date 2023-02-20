from collections import deque
# 어피치를 이기려면 
# 1. 어피치보다 1개 더 많이 쏘거나, 
# 2. 이 과녁에는 아예 0발을 쏘고 화살을 아껴서 다른 과녁의 승률을 높여주기

def bfs(n, info):
    res = [] # 최대점수차를 내는 화살 상황들을 모아둔 리스트
    q = deque([(0, [0]*11)])
    maxGap = 0

    while q:
        focus, arrow = q.popleft() # arrow는 현재 라이언 화살 상황

        if sum(arrow) == n: # 종료 조건 1) 화살을 다 쏜 경우
            apeach, lion = 0, 0 
            for i in range(11): # 점수 계산
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]: # 어피치가 같거나 크다면
                        apeach += 10-i
                    else: # 라이언이 크다면
                        lion += 10-i
            
            if apeach < lion: # 라이언이 이기면
                gap = lion - apeach
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap # 최대 점수차 갱신
                    res.clear()
                res.append(arrow)

        elif sum(arrow) > n: # 종료조건 2) 화살이 없는 경우
            continue

        elif focus == 10: # 종료조건 3) 화살이 남은 경우
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp) # 전부 마지막에 쏴줌 
            q.append((-1, tmp)) 
        
        else: # 화살 쏘기
            tmp = arrow.copy()
            tmp[focus] = info[focus]+1
            q.append((focus+1,tmp)) # 옵션1: 어피치보다 한발 많이 쏘기

            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus+1, tmp2)) # 옵션2: 0발 쏘기

    return res

def solution(n, info):
    winList = bfs(n, info)
    
    if not winList:
        return [-1]
    elif len(winList) == 1:
        return winList[0]
    else:
        return winList[-1] # 여러개면 가장 낮은 점수를 더 많이 맞힌 경우

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))