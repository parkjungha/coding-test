from collections import Counter, defaultdict
from itertools import combinations_with_replacement

def solution(k, n, reqs):
    answer = float('inf')
    
    # 중복조합으로 가능한 모든 경우 구하기 (n명의 멘토를 k개의 상담 유형에 배치하는 모든 경우의 수)
    cases = []
    for case in combinations_with_replacement([i for i in range(k)], r=n-k):
        base = [1 for i in range(k)]
        for c in case:
            base[c] += 1
        cases.append(base) 
    # n = 5, k = 3일때 cases는 [[3, 1, 1], [2, 2, 1], [2, 1, 2], [1, 3, 1], [1, 2, 2], [1, 1, 3]] 
 
    # 상담 유형 : [시작시간, 종료시간]
    participants = defaultdict(list)
    for start_time, minutes, category in reqs:
        participants[category].append([start_time, start_time + minutes])
        
    # 각 케이스에 대해 wait_time을 구하고 최소값 찾기
    for case in cases:
        wait_time = 0 

        for i in range(k): # 각 상담 유형 별로
            p_list = sorted(participants[i+1], key=lambda x:x[0]) # 시작 시간이 빠른 순으로 참가자 정렬 
            mento_list = [0 for _ in range(case[i])] # 현재 유형에 배치된 멘토에 대해서, 각 멘토의 상담 종료 시간 저장.
            
            for start_time, end_time in p_list: # 상담해야하는 각 참가자에 대해서 
                mento_list = sorted(mento_list) # 가장 빨리 끝나는 멘토 순서로 정렬
                if mento_list[0] <= start_time: # 참가자의 상담 시작 시간보다 멘토의 상담 종료 시간이 빠르면 
                    mento_list[0] = end_time # 기다리지 않고 상담 후 종료 시간 업데이트 
                else: # 참가자가 멘토의 상담 종료까지 기다려야 함
                    temp_t = mento_list[0] - start_time # 기다려야 하는 시간
                    mento_list[0] = end_time + temp_t # 상담 종료 시간 + 기다림 시간
                    wait_time += temp_t
                    
            # 만약 현재 최소값보다 길어지면 break
            if wait_time > answer:
                break
                
        if wait_time < answer: # 최소값 갱신
            answer = wait_time
            
    return answer
