from itertools import product
import copy

def solution(clockHands):
    answer = float('inf')
    n = len(clockHands)

    dx = [-1, 1, 0, 0, 0]
    dy = [0, 0, -1, 1, 0]

    def rotate(x, y, dir, arr):
        for i in range(5):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                arr[nx][ny] = (arr[nx][ny] + dir) % 4

    # product는 (0,1,2,3) 중에서 n개를 중복을 허용하여 뽑는 모든 경우의 수 반환
    for case in product(range(4), repeat=n):    # 첫째줄 최대 4번까지 회전 한다는 가정 하에 모든 경우의 수를 만든다.
        arr = copy.deepcopy(clockHands)

        for j in range(n):    # case 를 가지고 첫번째 줄만 회전 시킨다
            rotate(0, j, case[j], arr)

        result = sum(case)    # 첫번째 줄 조작 횟수의 합

        for i in range(1, n):    # 두번째 줄부터 체크
            for j in range(n):
                if arr[i-1][j]:    # 12시 가있지 않은 시계만 조작
                    temp = 4 - arr[i-1][j]    # 12시에 가도록 하기 위한 조작 횟수
                    rotate(i, j, temp, arr)    # 회전
                    result += temp    # 조작 횟수 누적

        if sum(arr[n-1]):    # 마지막 라인에 12시를 향하지 않는 시계가 있다면 
            continue    # pass

        answer = min(answer, result)    # 시계가 모두 12시를 가리킨다면 answer을 최솟값으로 갱신

    return answer

solution([[0,3,3,0],[3,2,2,3],[0,3,2,0],[0,3,3,3]])