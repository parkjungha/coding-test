import math 
# 각 서브트리의 루트 노드는 항상 가운데에 위치

def dfs(b, i, depth):
    if depth == 0: # 리프노드에 도달
        return True # 포화이진트리
    
    # 부모노드가 '0'일때, 왼쪽 또는 오른쪽 자식 노드가 '1'이면 포화 이진트리가 될 수 없음
    elif b[i] == '0':
        if b[i-depth] == '1' or b[i+depth] == '1': 
            return False

    # 좌우 자식 서브트리 탐색
    left = dfs(b, i - depth, depth // 2)
    right = dfs(b, i + depth, depth // 2)
    return left and right 

def solution(numbers):
    answer = []

    for num in numbers:
        b = bin(num)[2:] # 10진수 -> 2진수 변환
        
        # 포화 이진 트리 노드 개수 == (2**n)-1 자릿수를 가져야함.
        digit = 2 ** (int(math.log(len(b), 2)) + 1) - 1
        b = '0' * (digit - len(b)) + b # 2진수에서 왼쪽에 모자란 길이만큼 0 추가
        
        # 이진 포화트리로 표현할 수 있는지 확인
        result = dfs(b, len(b)//2, (len(b)+1) // 4)
        answer.append(1 if result else 0)

    return answer
