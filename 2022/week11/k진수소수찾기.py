def isPrime(n): # 소수 판별 함수
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    res = ''
    while n: # n을 k진법으로 변환
        res += str(n%k)
        n = n//k
        
    res = res[::-1].split('0') # 뒤집고 0을 기준으로 자름
    
    answer = 0
    for i in res:
        if len(i)>0 and isPrime(int(i)):
            answer += 1
    return answer
        
        
print(solution(110011, 10))