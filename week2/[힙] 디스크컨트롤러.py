import heapq
def solution(jobs):
    answer = 0
    time = 0
    start = -1
    heap = []

    i = 0
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= time: # 현재 시점에서 처리할 수 있는 작업들을 모두 힙에 넣을건데
                heapq.heappush(heap,[j[1],j[0]]) # 소요시간 기준으로 최소힙 만들기

        if heap:
            curr = heapq.heappop(heap) # 최소 소요시간인거 pop
            start = time 
            time += curr[0] # 소요시간만큼 time에 더해줌
            answer += time - curr[1] # 해당 job의 요청에서 종료까지 시간
            i += 1
        else: # 힙이 비어있으면 time++
            time += 1
    
    return answer//len(jobs)

