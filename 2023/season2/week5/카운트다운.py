# 최소의 다트 횟수로 점수를 완성하되, 같은 횟수라면 불 또는 싱글 횟수가 최대인 경우
def solution(target):

    # 싱글/불로 만들수 있는 점수와, 싱글/불로 만들 수 없는 점수를 나누어서 저장
    score_table = []
    score_table.append([i for i in range(1, 21)]) # 싱글로 만들 수 있는 점수
    score_table[0].append(50) # 불 점수

    # 더블, 트리플로 만들 수 있는 점수 
    doubleTriple = []
    for i in range(1, 21):
        for j in [2, 3]: 
            score = i*j
            if score > 20:
                doubleTriple.append(score)
    
    score_table.append(list(set(doubleTriple)))

    # 2차원 dp 배열 [시도 횟수, 최대 싱글/불 횟수 합] 저장
    dp = [[INF, 0] for _ in range(target + 1)]
    dp[0][0] = 0

    # 모든 점수 순회하면서
    for i in range(1, target + 1):
        for j in range(2): # 싱글/불로 만들수 있는 점수와, 싱글/불로 만들 수 없는 점수 각각에 대해서
            for k in range(len(score_table[j])):
                prev = i - score_table[j][k] # 남은 점수

                if prev < 0:
                    continue

                total, valid = dp[prev][0] + 1, dp[prev][1] + 1 - j

                if total < dp[i][0]:
                    dp[i] = [total, valid]
                    
                elif total == dp[i][0]: # 현재 최솟값과 동일한 시도 횟수라면 최대 싱글/불 횟수 저장
                    dp[i] = [total, max(dp[i][1], valid)]

    return dp[target]
