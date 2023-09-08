class Solution:
    # Return the length of the longest subarray, which is a mountain. else, 0
    # Run 89.95% Mem 67.78%
    def longestMountain(self, arr: List[int]) -> int:
        curLen = 1
        maxLen = 0
        up = True

        for i in range(len(arr)-1):
            if up and arr[i] < arr[i+1]: # 커지는 중
                curLen += 1

            elif curLen > 1 and arr[i] > arr[i+1]: # 바뀌는 지점
                up = False
                curLen += 1
                if curLen >= 3:
                    maxLen = max(maxLen, curLen) # 최대값 계속 갱신 

            elif not up and arr[i] < arr[i+1]: # 다시 증가 -> 새로운 mountain 가능 
                curLen = 2
                up = True

            else: # invalid 
                curLen = 1

        return maxLen 