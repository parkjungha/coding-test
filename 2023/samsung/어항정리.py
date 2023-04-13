# 2. 어항을 쌓는다
# (1) 가장 왼쪽에 있는 어항을 그 어항의 오른쪽에 있는 어항의 위에 올려놓는다
# (2) 2개 이상 쌓여있는 어항을 모두 공중 부양시킨 다음, 전체를 시계방향으로 90도 회전
# (3) 공중 부양시킨 어항을 바닥에 있는 어항의 위에 올려놓는다
# (1~3) 이 작업은 공중 부양시킨 어항 중 가장 오른쪽에 있는 어항의 아래에 바닥에 있는 어항이 있을때까지 반복
def stackBowl1(fishes, N):
    # 처음 회전은 hard coding
    bowl = fishes[:] # 복사
    rot = [[bowl[0]],[bowl[1]]]
    bowl = bowl[2:]

    # 두번째 회전부터
    while True:
        h = len(rot) # 높이
        w = len(rot[0]) # 밑변
        if len(bowl) >= h: # 남은 길이가 높이보다 클때만 회전 가능
            

# 1. 물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다
def fillFish(fishes, N):
    minFish = min(fishes)
    for i in range(fishes):
        if fishes[i] == minFish:
            fishes[i] += 1
    return fishes

def solve(fishes, N):
    fishes = fillFish(fishes, N)
    fishes = stackBowl1(fishes, N)
    fishes = stackBowl2(fishes, N)
    return fishes

# Main
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N, K = map(int,input().split())
fishes = list(map(int,input().split()))
ans = 0
while max(fishes) - min(fishes) > K:
    ans += 1
    fishes = solve(fishes, N)
print(ans)