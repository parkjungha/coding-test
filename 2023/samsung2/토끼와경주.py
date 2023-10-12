import heapq

Q = int(input())

# 100 N M P pid_1 d_1 pid_2 d_2 ... pid_p d_p
info = list(map(int,input().split()))[1:]
N,M,P = info[0], info[1], info[2]

rabbitHeap = []
scores = {}
distance = {}

minus_score = 0

for i in range(3, len(info), 2):
    heapq.heappush(rabbitHeap, [0,0,0,0,info[i]]) # 총 점프횟수, 행+열, 행, 열, 고유번호
    scores[info[i]] = 0
    distance[info[i]] = info[i+1]


orders = []
for _ in range(Q-1):
    orders.append(list(map(int,input().split())))

def isValid(nx,ny):
    return 0<=nx<N and 0<=ny<M

def outOfRange(nx, ny):
    nx %= 2*(N-1)
    ny %= 2*(M-1)
    return min(nx, 2*(N-1)-nx), min(ny, 2*(M-1)-ny)
    
def getLocation(x,y,d): 
    dx = [-1,0,1,0] # 상 좌 하 우
    dy = [0,-1,0,1] # 0이면 2, 1이면 3, 2이면 0, 3이면 1 
    candidates = []

    for i in range(4): # 상 하 좌 우 네방향으로 각각 d만큼 이동했을때의 위치
        nx = x + dx[i]*d
        ny = y + dy[i]*d

        if not isValid(nx, ny):
            nx, ny = outOfRange(nx, ny)
        
        candidates.append([nx, ny])        

    candidates.sort(key= lambda x: (x[0]+x[1], x[0], x[1]))
    return candidates[-1] # 우선순위가 가장 높은 칸 위치 [x,y] 반환

def getScore(pid, score):
    global minus_score
    minus_score += -(score + 2)
    scores[pid] += -(score + 2)

def run(K, S): # K번 반복, 점수 S
    pickedRabbit = []
    for _ in range(K):
        # 총 점프횟수, 행+열, 행, 열, 고유번호
        cnt, xy, x, y, pid = heapq.heappop(rabbitHeap) # 우선순위가 가장 높은 토끼의 위치 x,y와 이동거리 d, 고유번호 pid
        cnt += 1
        r, c = getLocation(x, y, distance[pid]) # 이동할 칸 위치

        getScore(pid, r+c) # pid 토끼 빼고 나머지 토끼 점수 얻음
        heapq.heappush(rabbitHeap, [cnt, r+c, r, c, pid])
        heapq.heappush(pickedRabbit, [-(r+c), -r, -c, -pid])

    d,um,my, pid = heapq.heappop(pickedRabbit)

    scores[-pid] += S
    return 

def changeD(pid, L):
    distance[pid] *= L
    return

def bestRabbit():
    score = -1
    for s in scores.values():
        score = max(score, s)
    return score - minus_score

for order in orders:
    if order[0] == 200: # 경주 진행
        run(order[1], order[2])

    elif order[0] == 300: # 이동 거리 정보 변경
        changeD(order[1], order[2]) # pid_t 토끼의 이동거리를 L 로 변경

    else:
        print(bestRabbit())


'''
(1) 경주 시작 준비

N*M 격자 , P 마리 토끼
i번 토끼 고유번호 pid_i, 이동해야하는 거리 d_i
처음 토끼 위치는 모두 (0,0) 

(2) 경주 진행: 우선순위가 높은 토끼를 뽑아 멀리 보내주는 것을 K번 반복

(2)-1. 우선순위가 높은 토끼 i 결정 
우선순위: (현재까지의 총 점프 횟수가 적은 토끼, 현재 서있는 행 번호 + 열 번호가 작은 토끼, 행 번호가 작은 토끼, 열 번호가 작은 토끼, 고유번호가 작은 토끼)

(2)-2. 토끼 이동
이동할 칸 (r_i,c_i) 결정: 네칸 중 우선순위에 따라 결정
상하좌우 네 방향으로 각각 d_i 만큼 이동한다고 할때,
4개의 위치 중 (행 번호 + 열 번호가 큰 칸, 행 번호가 큰 칸, 열 번호가 큰 칸) 순으로 이동
이동중 격자를 벗어나게 된다면 방향을 반대로 바꿔서 이동

(2)-3. 나머지 토끼들 점수 획득
 i번 토끼를 제외한 나머지 P−1마리의 토끼들 전부 (r_i+c_i)만큼 점수 획득

K번 턴 끝나고, 우선순위가 높은 토끼를 골라 점수 S 더해줌
우선순위: (현재 서있는 행 번호 + 열 번호가 큰 토끼, 행 번호가 큰 토끼, 열 번호가 큰 토끼, 고유번호가 큰 토끼)
한번이라도 뽑혔던 적이 있던 토끼중에서 골라야함

(3) 이동거리 변경
pid_t 인 토끼의 이동거리를 L배

(4) 가장 점수 높은 토끼의 점수 출력

'''