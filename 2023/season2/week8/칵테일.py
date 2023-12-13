# https://www.acmicpc.net/problem/1033

n = int(input())
pairs = [[] for _ in range(n)] # n-1개의 재료 쌍 비율 정보
visited = [False]*n
mass = [0]*n # 질량
lcm = 1 # 최소공배수

def gcd(a,b): # 최대공약수
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def dfs(a):
    visited[a] = True
    for i in pairs[a]:
        b = i[0] # 상대 재료 b
        if not visited[b]: 
            mass[b] = mass[a]*i[2] // i[1] # b질량 = (a질량*q) / p
            dfs(b)

for i in range(n-1):
    # a의 질량을 b의 질량으로 나눈 값이 p/q
    a, b, p, q = map(int, input().split())
    pairs[a].append((b,p,q))
    pairs[b].append((a,q,p))
    lcm *= ((p*q) // gcd(p,q)) # 최소공배수

mass[0] = lcm # 첫번째 재료 기준, 최소공배수로 설정
dfs(0) # 비율에 맞게 다른 숫자들 질량 설정

mgcd = mass[0] # 모든 수의 최대공약수 계산

for i in range(1,n):
    mgcd = gcd(mgcd, mass[i])

# 최대공약수로 각 질량 나누어줌
for i in range(n):
    print(int(mass[i]//mgcd), end = ' ') 