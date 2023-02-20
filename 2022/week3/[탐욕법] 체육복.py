def solution(n, lost, reserve):
    reserve_ = set(reserve) - set(lost) # 여벌 체육복을 가져온 학생이 체육복을 도난당한 경우
    lost_ = set(lost) - set(reserve) 
    
    answer = n - len(lost_) # 이미 체육복을 가진 학생의 수
    
    for l in lost_: # 잃어버린 학생 순회
        if l-1 in reserve_: # 앞뒤에 여벌옷이 있는지
            reserve_.remove(l-1) # 빌림
            answer += 1 
        elif l+1 in reserve_: 
            reserve_.remove(l+1)
            answer += 1
            
    return answer