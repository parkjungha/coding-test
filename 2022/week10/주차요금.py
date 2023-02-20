
import math
from collections import defaultdict

def solution(fees, records):
    answer = []
    dict = {} # 특정 차량 번호에 대한 주차 시간을 담을 임시 dict 딕셔너리
    total = defaultdict(int) # 총 주차 시간을 담을 total 딕셔너리

    for record in records:
        time, number, state = record.split()
        hour, minutes = time.split(":")
        time = int(hour)*60 + int(minutes)

        if number in dict: # 이미 입차되어 있다면
            total[number] += time - dict[number]
            del dict[number]
        else: # 입차할 경우
            dict[number] = time
        
    # 출차 안 한 경우
    max_time = (23*60) + 59
    for num, t in dict.items():
        total[num] += max_time - t
    
    # 요금 계산
    basic_minutes, basic_fee, split_minutes, split_fee = fees
    for num, t in total.items():
        cost = basic_fee # 기본요금
        if t > basic_minutes: # 추가요금
            cost += math.ceil((t-basic_minutes)/split_minutes) * split_fee
        answer.append((num,cost))

    # 차량 번호 오름차순
    answer.sort()
    return [value[1] for value in answer]