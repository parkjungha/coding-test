# 모든 팀은 최소 1명 이상의 직원을 워크숍에 참석
# 워크숍에 참석하는 직원들의 하루평균 매출액의 합이 최소

# 팀장이 참석 하는경우 / 하지 않는 경우

def solution(sales, links):
    link=[[] for _ in sales]
    dp=[[0,0] for _ in sales]
    for a,b in links: link[a-1].append(b-1)

    def solve(i):
        sum_child=0
        for k in link[i]: # 모든 팀장들 돌면서 
            solve(k)
            sum_child+=min(dp[k][0],dp[k][1])

        dp[i][1]=sum_child + sales[i]
        if any(dp[k][0]>dp[k][1] for k in link[i]):
            dp[i][0]=sum_child
        else:
            dp[i][0]=sum_child + min(
            (dp[k][1]-dp[k][0] for k in link[i]),
            default=0)
            
    solve(0)
    return min(dp[0][0],dp[0][1])
