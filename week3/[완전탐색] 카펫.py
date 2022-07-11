def solution(brown, yellow):
    total = brown + yellow
    for i in range(total,2,-1):
        if total % i == 0: # 가로 길이가 나누어 떨어지면 
            s = total // i # 세로
            if (i-2)*(s-2) == yellow:
                return [i,s]