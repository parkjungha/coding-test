'''
@ 이분 탐색(이진 탐색)
 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
 
@ 동작 방식
배열의 중간 값을 가져오기
중간 값과 검색 값을 비교
      2-1. 중간 값이 검색 값과 같다면 종료 (mid = key)

      2-2. 중간 값보다 검색 값이 크다면 중간값 기준 배열의 오른쪽 구간을 대상으로 탐색(mid < key)

      2-3. 중간 값보다 검색 값이 작다면 중간값 기준 배열의 왼쪽 구간을 대상으로 탐색 (mid > key)

   3. 값을 찾거나 비어 있을 때까지 반복

'''

def solution(n, times):
    answer = 0
    # right는 가장 비효율적으로 심사할 때 걸리는 시간
    left = min(times)
    right = max(times)*n
    
    while left <= right:
        mid = (left+right) // 2
        checked = 0
        for time in times:
            # people은 모든 심사관들이 mid 분동안 심사한 사람의 수 
            checked += mid // time
            # 모든 심사관을 거치지 않아도 mid 분 동안 n 명 이상의 심사를 할 수 있다면 반복문 나감
            if checked >= n:
                break
        
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
        if checked >= n:
            answer = mid
            right = mid -1 # 왼쪽 범위 탐색 

        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우
        elif checked < n:
            left = mid + 1 # 오른쪽 범위 탐색
    return answer