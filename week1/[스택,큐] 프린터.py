# 중요도가 같은 문서가 있으므로 인덱스를 저장하는게 관건 !
from collections import deque # 양쪽 끝에서 넣었다 뺐다하기 위해서 DEQUE사용

def solution(priorities, location):

    answer = 0 
    deq = deque([(val,idx) for idx,val in enumerate(priorities)]) # [(우선순위, 인덱스), ...]로 각 문서 저장
    
    while deq: # DEQUE가 빌 때까지
        temp = deq.popleft() # 앞에서 꺼내서
        if deq and temp[0] < max(deq)[0]: # 나머지 대기목록에서 중요도가 높은 문서가 한 개라도 존재하면
            deq.append(temp) # 맨뒤로 넣음
        else: # 중요도가 더 높은 문서가 없으면 
            answer += 1 # 처리 순서++
            if temp[1] == location: # 알고싶은 인덱스이면
                return answer