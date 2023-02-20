# 짝수인 경우, 가장 마지막 비트: 0 -> 1 즉 그냥 1 큰 숫자
# 홀수인 경우, 가장 뒤에 있는 0 -> 1, 그다음 비트 0으로

def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0: # 짝수
            answer.append(num+1)
        else: # 홀수
            bnum = '0'+bin(num)[2:]
            idx = bnum.rfind('0') # 가장 뒤에 있는 0 인덱스
            ans = bnum[:idx]+'10'+bnum[idx+2:]
            answer.append(int(ans,2)) 
            
    return answer

print(solution([2,7]))