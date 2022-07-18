# https://alreadyusedadress.tistory.com/115
# 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 
# N을 최소로 사용해서 number를 만드는 것이 목표
# 즉 1 ~ 8개의 N을 사용해서 만들 수 있는 수의 집합 중에 number가 처음 나오는 개수를 리턴

def solution(N, number):
    if number == 1:
        return 1

    set_list = []

    for cnt in range(1,9): # N=1개부터 8개까지 확인
        partial_set = set()
        partial_set.add(int(str(N) * cnt)) # 단순 이어붙여서 만드는 경우
        
        for i in range(cnt-1): # (1,n-1)부터 (n-1,1)까지 사칙연산
            for op1 in set_list[i]:
                for op2 in set_list[-i-1]: # 사칙연산
                    partial_set.add(op1+op2)
                    partial_set.add(op1-op2)
                    partial_set.add(op1*op2)
                    if op2 != 0:
                        partial_set.add(op1/op2)

        # 만든 집합에 number가 처음 나오는지 확인
        if number in partial_set:
            return cnt
        set_list.append(partial_set)

    return -1
    