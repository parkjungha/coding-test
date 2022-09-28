# 완전탐색 
# 문자열을 1개 단위로 자를때부터 ~ 문자열 길이 n개 단위로 자를때까지
def solution(s):
    result=[]
    
    if len(s)==1:
        return 1
    
    for i in range(1, len(s)+1):
        b = ''
        cnt = 1
        tmp=s[:i]

        for j in range(i, len(s)+i, i):
            if tmp == s[j:i+j]: # 앞과 같으면
                cnt+=1
            else: # 다르면
                if cnt != 1: 
                    b = b + str(cnt)+tmp
                else: # 1인경우 숫자 생략 
                    b = b + tmp
                    
                tmp=s[j:j+i]
                cnt = 1
                
        result.append(len(b))
        

    return min(result)
