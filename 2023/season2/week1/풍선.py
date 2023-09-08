# 자신의 왼쪽에 있는 모든 수의 최솟값, 오른쪽에 있는 모든 수의 최솟값 
# 둘 중 하나보다 자신이 작으면 남길 수 있음. 

def solution(a):
    result = [0 for _ in range(len(a))]
    minLeft, minRight = float('inf'), float('inf')
    for i in range(len(a)): # 숫자 하나씩 돌면서 살아남을 수 있는지 확인함
        if a[i] < minLeft: # 앞에서부터 시작
            minLeft = a[i] # 최소값 갱신
            result[i] = 1 # 살아남을 수 있다
        
        if a[-1-i] < minRight: # 뒤에서부터 시작:
            minRight = a[-1-i] 
            result[-1-i] = 1

    return sum(result)