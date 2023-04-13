
from copy import deepcopy

N, K = map(int,input().split())
robots = []
belts = list(map(int,input().split()))
belts.insert(0, -1) # dummy: 1~2N까지의 index
is_robot = [0 for _ in range(len(belts))] # 해당 belts의 index에 로봇이 있는지 없는지

def rotate():
    global belts, is_robot, robots
    # 벨트 회전
    n = belts.pop() # 맨뒤에거 
    belts.insert(1, n) # 맨앞으로 넣음

    # 로봇 회전
    new_robot = []
    is_robot = [0 for _ in range(len(belts))]
    for idx in robots: # 기존 로봇들 위치 반환
        new_idx = idx + 1 # 이동할 다음칸
        if new_idx < N: # 이동 가능
            new_robot.append(new_idx)
            is_robot[new_idx] = 1
    robots = deepcopy(new_robot) # 로봇 정보 update

def move_robot():
    global is_robot, robots, belts
    for i in range(len(robots)):
        new_idx = robots[i]+1 # 이동할 다음칸
        if not is_robot[new_idx] and belts[new_idx] >= 1: 
            belts[new_idx] -= 1 # 내구도 감소
            is_robot[robots[i]] = 0 # 현재 인덱스 로봇 사라짐
            if new_idx != N: 
                robots[i] += 1 # 이동해줌
                is_robot[new_idx] = 1

def insert_robot():
    # 1번째 칸에 로봇 추가 
    global is_robot, robots
    if belts[1] != 0:
        robots.append(1)
        belts[1] -= 1
        is_robot[1] = True

step = 0
while True:
    step += 1
    rotate()
    move_robot()
    insert_robot()
    if belts.count(0) >= K:
        break
    
print(step)

