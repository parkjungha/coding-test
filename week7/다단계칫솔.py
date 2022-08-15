
def solution(enroll, referral, seller, amount):

    ans_dic = dict(zip(enroll, [0]*len(enroll))) # 정답 저장할 dictionary 
    ref_dic = dict(zip(enroll, referral)) # 추천인 정보 저장할 dictionary
    
    for i in range(len(seller)): # 모든 판매 집계 데이터에 대해서 하나씩 계산
        value = amount[i]*100 # 수익금 돈
        seller_name = seller[i]
        
        while True:
            if value < 10: # 10%를 계산한 금액이 1 원 미만인 경우에는 모두 가지고 종료
                ans_dic[seller_name] += value
                break
            
            else: # 10% 수익 배분
                ans_dic[seller_name] += value - (value//10)
                if ref_dic[seller_name] == "-":
                    break
                value = value//10
                seller_name = ref_dic[seller_name]
                
    return list(ans_dic.values())

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	,["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]	,["young", "john", "tod", "emily", "mary"]	, [12, 4, 2, 5, 10]	))