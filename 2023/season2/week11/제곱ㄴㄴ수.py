# min부터 max까지 하나씩 돌면서, 제곱수 하나씩 (4, 9, 16, ...) 보면서 count 하면 무조건 시간초과
# 반대로 min ~ max 범위만큼의 Bool 배열에서 미리 제곱수의 배수들을 모두 걸러낸다
# 걸러진 수(True)는 제곱수로 나누어지는 수. 안걸러진(False) 수가 제곱ㄴㄴ수

minV,maxV = map(int, input().split())

ans = maxV - minV + 1 # min ~ max 사이 수 전부
check = [False]*(maxV - minV + 1)
n = 2
while n*n <= maxV:
    nn = n*n # 제곱수 (4, 9, 16, 25, ... )
    if minV % nn == 0: # 나누어떨어지면 
        remain = 0
    else: remain = 1

    i = minV // nn + remain # 범위 내에 속하는 배수부터 시작

    while nn*i <= maxV: # 제곱수에 i배
        if not check[nn*i - minV]: 
            check[nn*i - minV] = True # 제곱수로 나누어지는 수  
            ans -= 1 
        i += 1 # 곱할 배수 1씩 증가
    n += 1 # 제곱수도 1씩 증가

print(ans)
