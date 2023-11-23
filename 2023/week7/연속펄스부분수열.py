def solution(sequence) :
    s1, s2 = [], []
    pulse = 1
    for i in sequence:
        s1.append(i*pulse)
        pulse *= -1
        s2.append(i*pulse)
    
    def max_prefix(arr): # 부분 수열의 합의 최대값 찾기
        prefix = [0]
        for i in arr: # i번째 인덱스를 끝점으로하는 음수가 되지 않는 부분 수열의 합
            prefix.append(max(0, prefix[-1]) + i)
        return max(prefix)
    
    answer = max(max_prefix(s1), max_prefix(s2))
    return answer