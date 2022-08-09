def solution(distance, rocks, n):
    answer = 0
    left, right = 0, distance
    rocks.append(distance)
    rocks.sort()

    while left <= right:
        mid = (left+right) // 2 # 기준 값
        current, remove = 0,0 # 현재 위치, 제거할 바위 수 
        min_dist = float('inf') # mid에서 최소 거리

        # 거리 구하기
        for rock in rocks:
            dis = rock - current
            if dis < mid:
                remove += 1
            else:
                current = rock
                min_dist = min(min_dist, dis)

        if remove > n: # n보다 많으면 mid를 줄임
            right = mid -1 # 왼쪽 탐색
        else: # n보다 많지 않으면 최소거리를 answer에 저장하고 mid를 늘림
            answer = min_dist
            left = mid + 1 #오른쪽 탐색
    return answer