# 행과 열 인덱스 중 더 큰 거 +1
# 행은 i//n 열은 i%n로 표현해서 효율성 통과


def solution(n, left, right): # 완전탐색 -> 효율성 통과 XXX
    answer = []
    for i in range(n): # 행 
        for j in range(n): # 열
            answer.append(max(i,j)+1)

    return answer[left:right+1]

def solution(n, left, right): # 규칙 찾기
    answer = []
    for i in range(left, right+1):
        answer.append(max(i//n, i%n)+1)
    
    return answer