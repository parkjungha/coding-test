
def solution(routes):
    # 1. route[1] 기준으로 정렬
    routes = sorted(routes, key= lambda x: x[1]) # 진출 지점 기준으로 정렬 
    
    # 2. 카메라 위치 초기화
    prev_cam = -30000
    answer = 0

    # 3. routes 순회
    for route in routes: 
        if prev_cam < route[0]: # 차량의 진입지점보다 최근 카메라 위치와 안겹치면 
            answer += 1 # 카메라 하나 더 세움 
            prev_cam = route[1] # 최근 카메라 위치는 차랑의 진출지점으로 갱신

    return answer