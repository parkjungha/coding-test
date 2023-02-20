# 이진탐색!!!!!!!!!!!!!!!!!!!! 어려워

def solution(a, b, g, s, w, t):
    # 최악의 경우
    # 광물의 최대 무게: 10**9
    # 도시의 최대 개수: 10**5
    # 왕복 2
    # 한 도시에 금, 은만 각각 있을 경우 2
    answer = (10**9) * (10**5) * 4
    end = (10**9) * (10**5) * 4
    start = 0
    
    while start <= end:
        mid = (start + end) // 2
        gold = 0
        silver = 0
        total = 0

        for i in range(len(g)):
            # 현재 정보
            now_gold = g[i]
            now_silver = s[i]
            now_weight = w[i]
            now_time = t[i]

            # 주어진 시간 내에서 이동할 수 있는 횟수 (왕복)
            move_cnt = mid // (now_time * 2)

            # 편도 추가
            if mid % (now_time * 2) >= now_time:
                move_cnt += 1

            # 현재 마을에 있는 금의 무게가 한번에 운반할 수 있는 양보다 적으면 그걸 더해주고, 아니라면 운반 가능한 양을 더해준다
            gold += now_gold if (now_gold < move_cnt*now_weight) else move_cnt * now_weight
            silver += now_silver if (now_silver < move_cnt * now_weight) else move_cnt * now_weight
            
            total += now_gold + now_silver if (now_gold + now_silver < move_cnt * now_weight) else move_cnt * now_weight
            # 금과 은 둘의 무게를 더한 게 한번에 나를 수 있는 양보다 큰지 확인. 초과하면 운반 가능한 양만 더해준다

            # 기준과 비교해서 왼쪽 탐색할지 오른쪽 탐색할지 이분 탐색 수행 
        if gold >= a and silver >= b and total >= a+b:
            end = mid -1
            answer = min(answer, mid)
        else:
            start = mid+1

    return answer