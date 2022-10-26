import heapq

def solution(lines):
    answer = 0
    period = []
    # "2016-09-15 20:59:57.421 0.351s"
    for line in lines:
        dtime = line[11:] # "20:59:57.421 0.351s"
        ed_last = dtime.split(' ')
        ed = ed_last[0] # "20:59:57.421" 응답완료 시간
        last = float(ed_last[1][0:-1]) # "0.351s" 처리시간
        sec = float(ed[0:2]) * 3600.0 + float(ed[3:5]) * 60.0 + float(ed[6:])
        period.append((sec-last+0.001, sec)) # (시작시간, 끝시간) 구간 리스트

    period.sort(key=lambda t: t[0]) # 시작시간 기준 정렬

    pq = []

    for time in period:
        st = time[0]
        while pq:
            if st-1 >= pq[0]: # {구간의 시작 시간 - 1초} 값이 우선순위 큐의 TOP원소의 종료시간보다 같거나 크면 구간이 겹치지 않는다는 뜻
                heapq.heappop(pq)
            else:
                break
        heapq.heappush(pq, time[1]) # 종료시점에 대해 오름차순 정렬
        answer = max(answer, len(pq))

    return answer

print(solution([
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]))