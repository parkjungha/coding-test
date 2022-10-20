
def solution(n, t, m, timetable):

    timetable = sorted(timetable, reverse=True) # 정렬
    timetable = [int(time[:2])*60 + int(time[3:]) for time in timetable] # 분단위로 변환
    
    for i in range(n): # 셔틀 버스 n번 온다
        arriveTime = 540 + i*t # t분 간격
        cnt = 0
        while timetable:
            if timetable[-1]  > arriveTime or cnt >= m: # 도착시간에 아무도 안왔거나, m명을 이미 태웠을때
                break
            lastTime = timetable[-1] # 제일 빨리 온 사람
            timetable.pop() # 태울수있는사람 태운다
            cnt += 1

        if i == n-1 : # 마지막 버스이면 콘 태워야함. 
            if cnt < m: # 마지막 셔틀버스의 탑승 인원이 m명보다 작다면
                answer = arriveTime # 마지막 버스의 도착시간에 탄다
            else: # 꽉 찼으면
                answer = lastTime - 1 # 마지막으로 탑승한 크루보다 1분 일찍 탄다
            return "%02d:%02d"%(answer//60, answer%60)