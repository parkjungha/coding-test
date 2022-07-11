from itertools import permutations
def solution(numbers):
    answer = []
    nums = list(numbers)
    per = []
    for i in range(1, len(nums)+1):  # 순서가 있는 가능한 모든 조합 (순열) 만들기
        per += list(permutations(nums,i)) 
    new_nums = [int(("").join(p)) for p in per] # 각 순열조합을 합치고 정수로 만들기

    for n in new_nums: # 만들어진 모든 숫자에 대해서 
        if n<2: # 2보다 작으면 소수가 아님 
            continue
        check = True # 소수 판단 bool
        for i in range(2,n): 
            if n%i == 0:
                check = False
                break
        if check:
            answer.append(n)

    return len(set(answer))