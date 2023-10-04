def solution(a, b, g, s, w, t):
    # 금 a 은 b 필요
    # 금정보 g, 은정보 s, 시간정보 t, 최대무게정보 w
    # 최소 시간 Return 
    answer = (10**9) * (10**5) * 4

    # 시간을 기준으로 이분탐색
    # right의 초기값은 최악의 경우, 
    # 광물 최대 무게 10^9 * 도시 최대 개수 10^5 * 왕복 2 * 금과 은2
    left = 0
    right = (10**9) * (10**5) * 4

    while left <= right:
        mid = (left + right) // 2
        gold = 0
        silver = 0
        total = 0

        for i in range(len(g)): # 각 도시 i 에 대해서
            # 현재 도시 정보
            curr_g, curr_s, curr_w, curr_t = g[i], s[i], w[i], t[i]

            # 주어진 시간 내에서 이동할 수 있는 횟수 (왕복)
            move_cnt = mid // (curr_t*2)

            if mid % (curr_t*2) >= curr_t: # 마지막은 편도
                move_cnt += 1

            amount = move_cnt * curr_w # 한번에 운반할 수 있는 양
            if curr_g < amount: # 금의 무게가 한번에 운반할 수있는 양보다 적으면
                gold += curr_g # 금의 무게 더해줌
            else:
                gold += amount # 운반 가능한 양만 더해줌

            if curr_s < amount:
                silver += curr_s
            else:
                silver += amount

            if curr_g + curr_s < amount:
                total += (curr_g + curr_s)
            else: # 금과 은의 무게를 더한게 한번에 운반할 수 있는 양보다 크면
                total += amount 

        if gold >= a and silver >= b and total >= a+b:
            right = mid -1
            answer = min(answer,mid) # 최소 시간 갱신
        else: 
            left = mid + 1
            
    return answer


#https://bladejun.tistory.com/166
