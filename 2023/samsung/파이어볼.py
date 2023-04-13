from copy import deepcopy
from collections import defaultdict

N, M, K = map(int,input().split())
balls = defaultdict(list)
for _ in range(M):
    r,c,m,s,d = map(int,input().split())
    balls[(r-1,c-1)].append((m,s,d))

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def move_ball():
    global balls
    new_balls = defaultdict(list)
    for loc, info in balls.items():
        x,y = loc
        for m,s,d in info:
            nx = (x + dx[d]*s)%N
            ny = (y + dy[d]*s)%N
            new_balls[(nx,ny)].append((m,s,d))

    balls = new_balls

def fireball():
    global balls
    new_balls = defaultdict(list)
    for loc, info in balls.items():
        x,y = loc
        if len(info) == 1: 
            new_balls[loc].append(info[0])
            continue

        sumM, sumS, sumN, sumD = 0,0,len(info),True
        evenOdd = info[0][2] % 2 # 첫번째값이 홀수인지 짝수인지 기준
        for m,s,d in info: # 같은 칸에 있는 ball에 대해서 질량,속력,방향 정보 합산
            sumM += m
            sumS += s
            if evenOdd != d%2: # 한번이라도 다르면 False로 바뀜
                sumD = False
        if sumM // 5 == 0: # 질량이 0이면 소멸
            continue

        for i in range(0,8,2): # 파이어볼 네개 삽입
            if sumD:
                new_balls[loc].append((sumM//5, sumS//sumN, i))
            else:
                new_balls[loc].append([sumM//5, sumS//sumN, i+1])
            
    balls = new_balls # 파이어볼 정보 update
        
# Main
for _ in range(K): # K번 이동 명령
    move_ball()
    fireball()

ans = 0
for v in balls.values():
    for m in v:
        ans += m[0] # 질량 합산
print(ans)