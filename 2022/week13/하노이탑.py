# n개의 원판을 옮기기 위해서는
# 1번 출발, 2번 중간, 3번 도착 기둥일 때
# 1. n-1개의 원판을 1번에서 2번으로 옮긴다 (재귀)
# 2. n번째 원판을 1번에서 3번으로 옮긴다
# 3. n-1개의 원판을 2번에서 3번으로 옮긴다 (재귀)

def solution(n):
    def hanoi(n, src, dst, mid): # 원판 개수, 출발, 도착, 중간 기둥
        if n == 1: # 재귀 종료조건
            answer.append([src, dst]) # 이동 순서 [출발 , 도착]
            return
        hanoi(n-1, src, mid, dst) # n-1개 원판 1번에서 2번으로 옮기기
        answer.append([src, dst]) # n번째 원판 1번에서 3번으로 옮기기
        hanoi(n-1, mid, dst, src) # n-1개 원판 2번에서 3번으로 옮기기

    answer = []
    hanoi(n, 1, 3, 2)
    return answer