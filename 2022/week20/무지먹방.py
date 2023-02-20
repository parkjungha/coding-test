# 효율성 무시
def solution(food_times, k):
    answer = -1
    index=0
    second=0
    
    while second <= k:
        index = index % len(food_times)
        if sum(food_times) == 0:
            return -1
        if food_times[index] != 0:
            food_times[index] -= 1
            second+=1
        index+=1
        
    return index

# 효율성 통과
import heapq
def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 heapq에 삽입 -> 빨리 먹을 수 있는 음식 순서대로 정렬
        heapq.heappush(q, (food_times[i], i+1))
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다먹은 음식 시간
    length = len(food_times) # 남은 음식 개수

    # k초 이내에 최대한 다 먹을 수 있는 음식을 한번에 먹음
    while sum_value + ((q[0][0] - previous)*length) <= k:
        now = heapq.heappop(q)[0] # 현재 음식 시간
        sum_value += (now-previous)*length
        length -= 1 # 다먹은 음식 제외
        previous = now

    # 남은 음식 중에서 몇번째 음식인지 확인하여 출력함
    result = sorted(q, key = lambda x:x[1]) # 음식 번호 기준 정렬
    return result[(k-sum_value)%length][1] # 번호 기준으로 남은 초 수 만큼 반복
