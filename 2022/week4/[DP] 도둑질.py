# dp[i] = max((바로 전 집까지 훔칠 수 있는 최댓값), (전전집까지의 훔칠 수 있는 최댓값 + 현재 집의 money))
# 1번 집을 털 경우: 2번부터 마지막 바로 전 집까지 훔칠 수 있는 돈 계산(마지막 집은 털지 못함)
# 1번 집을 털지 않을 경우: 2번부터 마지막 집까지 훔칠 수 있는 돈 계산

def solution(money):
    dp1 = [0]*len(money)
    dp2 = [0]*len(money)

    # 1번 집을 터는 경우
    dp1[0] = money[0]
    for i in range(1, len(money)-1): # 마지막 집은 털지 못함
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])
    
    # 1번 집을 안터는 경우
    dp2[0] = 0
    for i in range(1,len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])
    
    return max(dp1[-2], dp2[-1])