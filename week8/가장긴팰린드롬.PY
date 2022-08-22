
def solution(s):
    answer = 0
    for i in range(len(s)): # 앞부터
        for j in range(len(s),i,-1): # 뒤부터
            if s[i:j] == s[i:j][::-1]: # 팰린드롬이면
                answer = max(answer, len(s[i:j])) # 가장 긴 값 갱신
    return answer
