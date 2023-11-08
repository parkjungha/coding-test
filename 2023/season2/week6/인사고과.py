# 인센티브 못받는 사람을 O(N^2)으로 제거하면 시간 초과

def solution(scores):
    answer = 0
    target_a, target_b = scores[0] # 완호의 점수
    target_score = target_a + target_b

    # 첫번째 점수에 대해서 내림차순,
    # 첫 번째 점수가 같으면 두 번째 점수에 대해서 오름차순으로 정렬
    scores.sort(key=lambda x: (-x[0], x[1]))
    maxb = 0
    
    for a, b in scores:
        # 뒤에 있는 학생의 두 번째 점수가 앞에 학생의 두 번째 점수보다 작다면, 뒤 학생은 두 점수 모두 낮은 것. 인센티브 못받는 사람을 O(N)으로 탐색
        if target_a < a and target_b < b:
            return -1
        
        if b >= maxb:
            maxb = b
            if a + b > target_score:
                answer += 1
            
    return answer + 1
