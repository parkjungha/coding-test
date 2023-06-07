class Solution:
    # Monotonic Stack 모든 원소들이 오름차순(혹은 내림차순)을 유지하도록 하는 스택 구조

    # Run 81.91% (456ms) Mem 50.59% (20.8MB)
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # arr에 존재하는 모든 sub array의 min 값의 합
        stack = []
        res = 0
        prevsum = 0

        # number of subarrays that contain a specific element in a given range.
        # For an element, it will be element * count of subarrays where it is smallest
        # sum this amount for every element to get the answer.
        # with a monotonic stack

        for idx, val in enumerate(arr):
            cnt = 1
            while stack and stack[-1][0] >= val: # stack이 비어있지 않고 Top의 값이 현재 값보다 크거나 같을때
                v, c = stack.pop() # pop으로 제거 
                cnt += c 
                prevsum -= v*c

            stack.append((val, cnt)) # 최소값 push
            prevsum += val*cnt # element * count of subarrays where it is smallest
            res += prevsum
        
        return res % (10**9+7)
