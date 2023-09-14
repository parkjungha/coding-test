# 1) 스타수열은 짝수개
# 2) 스타 수열을 구성하는 각 쌍마다 공통 값이 최소 한개는 있어야함.
# 3) 쌍이 같은 값이면 안됨
# 즉, a 배열에 있는 모든 원소에 대해서, 해당 원소가 공통 값으로 적용되는 스타 수열 길이 찾기

from collections import Counter

def solution(a):
    answer = -1
    num_dict = Counter(a) # a에 있는 각 원소의 등장 횟수 count

    # a에 있는 각 원소 k를 기준으로 스타 수열을 만들 수 있는지 확인
    for k in num_dict.keys():
        # 시간 초과 방지
        # k의 등장 횟수가 이미 찾은 스타 수열의 공통 값 등장 횟수보다 작으면 바로 넘어간다
        if num_dict[k] < answer:
            continue 

        cnt = 0 # 기준이 되는 공통 값 k가 스타 수열안에 사용된 횟수 
        idx = 0 # 배열 탐색을 위한 인덱스

        while idx < len(a)-1:
            # 조건에 만족하지 않을 경우 다음 idx로 넘어가서 탐색한다
            # 1) a[idx]와 a[idx+1] 둘다 공통 값 k가 없는 경우
            # 2) a[idx]와 a[idx+1] 가 같은 경우
            if (a[idx] != k and a[idx+1] != k) or (a[idx] == a[idx+1]):
                idx += 1
                continue
            
            # 스타수열 원소로 추가할 수 있는 경우, k 원소가 사용된 횟수를 증가시킴
            cnt += 1

            # 다음 배열 탐색을 위해서 idx 2 증가
            idx += 2
        
        # 스타 수열에 사용된 공통 원소 최대값 갱신
        answer = max(answer, cnt)

    if answer == -1:
        return 0
    else: 
        # 공통 원소의 개수가 answer개니까, 실제 배열 길이는 2배
        return answer*2 

