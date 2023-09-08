class Solution:
    # 지난주 max Area와 유사한 Two pointer 접근법
    # Run 55.3% (133ms) Mem 74.54% (15.9MB)
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_of_Min = 0
        min_height = 0
        ans = 0

        while left < right:
            min_height = min(height[left], height[right])
            max_of_Min = max(max_of_Min, min_height)
            ans += max_of_Min - min_height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return ans

    # DP 풀이 
    # Run 39.79% (144ms) Mem 74.54% (15.9MB)
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        dp1, dp2 = [0 for _ in range(n)], [0 for _ in range(n)] # max height of bar from left / right to position i.

        # for each position i, if the current height is greater than the max height, 
        # then dp1[i] will be height[i]
        # else dp1[i] will be taking the previous result, dp[i-1]
        dp1[0] = height[0]
        for i in range(1, n):
            dp1[i] = max(height[i], dp1[i-1])

        # similar way for dp2
        dp2[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            dp2[i] = max(dp2[i+1], height[i])
    
        # for each position i, take min of dp1[i] and dp2[i]
        # substract height[i] from the min value
        # why min? that is the max height a bar can hold.
        for i in range(1, n-1):
            ans += min(dp1[i], dp2[i]) - height[i]

        return ans

    # Time Optimized Two pointer
    # Run 85.9% (119ms) Mem 74.54% (15.9MB)
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        leftmax = 0
        rightmax = 0
        ans = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    ans += leftmax - height[left]
                left += 1
            else:
                if height[right] > rightmax:
                    rightmax = height[right]
                else:
                    ans += rightmax - height[right]
                right -= 1
        return ans