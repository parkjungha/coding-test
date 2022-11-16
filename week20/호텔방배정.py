# 효율성 무시 

def solution2(k, room_number):
    answer = [0]*len(room_number)
    for i in range(len(room_number)):
        if room_number[i] not in answer: # 이미 차지한 방이 아니면
            answer[i] = room_number[i] # 배정해줌
        else:
            # room_number[i] 보다 번호가 크면서 answer에 없는 가장 작은 번호
            for x in range(room_number[i]+1, k+1):
                if x not in answer:
                    answer[i] = x
                    break
    return answer

# 효율성 고려
import sys
sys.setrecursionlimit(10000000)
def findEmptyRoom(num, rooms):
    if num not in rooms: # 아직 빈방
        rooms[num] = num + 1 # 부모노드 = 현재 방 번호 +1
        return num # 즉시 배정

    # 이미 그 방이 배정된 경우
    empty = findEmptyRoom(rooms[num], rooms) # 재귀로 빈방 찾기
    rooms[num] = empty + 1 # 부모노드 업데이트
    return empty # 빈방 번호 반환

def solution(k, room_number):
    answer = []
    rooms = {} # 방 체크 딕셔너리
    for num in room_number:
        emptyRoom = findEmptyRoom(num, rooms)
        answer.append(emptyRoom)
    return answer

print(solution(10, [1,3,4,1,3,1]	))