# 행과 열 인덱스 중 더 큰 거 +1
# 행은 i//n 열은 i%n로 표현해서 효율성 통과

def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        answer.append(max(i//n, i%n)+1)
    
    return answer