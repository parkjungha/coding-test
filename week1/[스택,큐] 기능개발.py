def solution(progresses, speeds):
    answer = []
    
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        cnt = 0
        while progresses and progresses[0] >= 100: # 맨 앞에 있는 기능이 완성되었으면
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        
        if cnt>0: # 배포할 기능이 하나 이상일 때
            answer.append(cnt)
        
    return answer