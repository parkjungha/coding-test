import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville)>1 and scoville[0] < K: # 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복
        answer += 1
        new = heapq.heappop(scoville) + (2*heapq.heappop(scoville))
        heapq.heappush(scoville, new)
    
    if scoville[0] < K: # 
        return -1 
    
    return answer

