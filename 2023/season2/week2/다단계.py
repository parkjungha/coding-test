def solution(enroll, referral, seller, amount):
    answer = [0]*len(enroll)

    dict = {} # Dictionary {사람이름:인덱스번호} 
    for i, e in enumerate(enroll):
        dict[e] = i

    for s, a in zip(seller, amount):
        m = a * 100 
        while s != "-" and m > 0: # 추천인이 없을때까지, 10% 떼줄 값이 있을때까지 반복
            idx = dict[s] # 현재 seller의 인덱스번호
            answer[idx] += (m - m//10) # 90% 만큼 더해줌
            m //= 10 # 10%는 추천인에게 올려줌
            s = referral[idx] # 추천인
    return answer
