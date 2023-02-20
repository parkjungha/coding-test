
from collections import deque

def solution(begin, target, words):
    if target not in words: # target이 words에 없으면 바로 리턴 0
        return 0

    q = deque()
    q.append((begin,0)) # # 큐에 시작 단어와 변환 횟수 담기

    while q: # 큐가 빌 때까지 반복
        temp, step = q.popleft()
        
        for word in words:
            diff = 0
            # 현재 단어와 딱 한글자만 차이나는 단어들만 찾기
            for i in range(len(temp)): 
                if temp[i] != word[i]:
                    diff += 1

            if diff == 1: # 한 글자만 차이나는 단어일때
                if word == target: # 찾은 단어가 Target이면
                    return step+1 # 바로 리턴
                q.append((word, step+1)) # 아니면 Queue에 넣기

    return 0