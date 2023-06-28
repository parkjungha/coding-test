class Solution:
    # TLE in TC 37 
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxVal = []
        for i in range(len(nums)-k+1):
            maxVal.append(max(nums[i:i+k]))
            
        return maxVal 
    
    # Deque 사용 Rumtime 81.48% Memory 66.21%
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque() # index 값 저장 - 맨 첫번째 값은 maximum 값
        result = []

        for i in range(len(nums)):
            # window 범위에 벗어나는 인덱스는 deque에서 삭제
            while window and window[0] <= i-k:
                window.popleft()
            
            # 오른쪽부터 현재 값보다 작으면 다 삭제
            while window and nums[window[-1]] < nums[i]: 
                window.pop()
            
            # 현재 값 삽입
            window.append(i)

            # 현재 윈도우의 가장 큰 값 result에 추가
            if i >= k-1:
                result.append(nums[window[0]])

        return result