from itertools import combinations
from collections import defaultdict

def solution(infos, queries):
    answer = []
    info_dict = defaultdict()
    for info in infos:
        info = info.split() # "java backend junior pizza 150"
        info_key = info[:-1] # "java backend junior pizza"
        info_val = int(info[-1]) # 150
        for i in range(1,5):
            for c in combinations(info_key, i): # 하나의 info에서 경우의 수 16개 만들기
                tmp_key = ''.join(c) 
                info_dict[tmp_key].append(info_val) # Key: 가능한 info의 조합, value: 점수
    
    for key in info_dict.keys():
        info_dict[key].sort() # value 값 점수들 오름차순 정렬

    for query in queries: # java and backend and junior and pizza 100
        query = query.split(" and ")
        query_score = query[-1].split()[1] # 100
        query[-1] = query[-1].split()[0]

        # java backend junior pizza
        while '-' in query: # - 제거
            query.remove('-')
        tmp_q = ''.join(query) # 찾을 쿼리 str으로

        # 이분탐색 lowerbound 사용해서 query_score보다 큰 점수들의 개수 구하기
        if tmp_q in info_dict:
            scores = info_dict[tmp_q]
            if len(scores)>0: 
                start, end = 0, len(scores)
                while end > start: 
                    mid = (start + end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid+1
                answer.append(len(scores)-start)
        else:
            answer.append(0)
    return answer