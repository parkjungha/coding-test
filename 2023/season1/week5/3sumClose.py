class Solution:
    # Runtime 90.6% (746ms) Memory 53.28% (14MB)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        sumVal = 0
        for i in range(len(nums)):
            l,r = i+1, len(nums)-1
            while l<r:
                s = nums[l] + nums[i] + nums[r]
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    return target

                if abs(s-target) < diff:
                    diff = abs(s-target)
                    sumVal = s
                    
        return sumVal 