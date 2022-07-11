
def solution(people, limit):
    answer = 0
    people.sort() # 몸무게순으로 정렬
    start, end = 0, len(people)-1 # 투포인터

    while start <= end: # 가장 무거운사람, 가벼운사람을 태울 수 있다면
        if people[start] + people[end] <= limit:
            start += 1 # 둘다 태움 
        end -= 1 # 아니면 무거운 사람만 태움 
        answer += 1 # 보트 개수 count
        
    return answer