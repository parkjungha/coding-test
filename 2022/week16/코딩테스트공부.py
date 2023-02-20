def solution(alp, cop, problems):
    max_alp_req, max_cop_req = [0, 0]

    for problem in problems: # 목표
        max_alp_req = max(max_alp_req, problem[0])
        max_cop_req = max(max_cop_req, problem[1])
    
    # dp[i][j]: 알고력 i, 코딩력 j을 도달 할 수 있는 최단시간
    dp = [[float('inf')]*(max_cop_req + 1) for _ in range(max_alp_req + 1)]
    
    # 시간 복잡도를 위해 목표 알고력을 넘는 알고력은 목표 알고력으로
    # 목표 코딩력을 넘는 코딩력은 목표 코딩력으로 계산하도록 처리하는 것
    alp = min(alp, max_alp_req)
    cop = min(cop, max_cop_req)
    dp[alp][cop] = 0 # dp[초기 알고력][초기 코딩력] = 0

    for i in range(alp, max_alp_req + 1):
        for j in range(cop, max_cop_req + 1):
            if i < max_alp_req: # 알고력 공부
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < max_cop_req: # 코딩력 공부
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)

            # 문제 풀기
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i+alp_rwd, max_alp_req)
                    new_cop = min(j+cop_rwd, max_cop_req)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)

    return dp[max_alp_req][max_cop_req]  # dp[목표 알고력][목표 코딩력]                   

# 시간 복잡도는 O(목표 알고력 * 목표 코딩력 * (problems 배열의 길이))