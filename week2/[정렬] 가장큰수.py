# 핵심 아이디어: 문자열 길이를 3배로 늘린 후에 비교하는 방식 ( 원소가 1000이하이므로 )

def solution(numbers):
    numbers_ = list(map(str, numbers))
    numbers_.sort(key = lambda x:x*3, reverse=True) # 인자 각각의 문자열을 3번 반복 -> 3자리수로 맞춘 뒤, 비교
    answer = ''
    answer = answer.join(numbers_) 
    return str(int(answer)) # 모든 값이 0일 때(즉, '000'을 처리하기 위해) int로 변환한 뒤, 다시 str로 변환한다. 
 