# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = 0
        for i in range(len(nums)):
            num += nums[i]
            for j in range(i+1, len(nums)):
                num += nums[j]
                if num == target:
                    return [i,j]
                num -= nums[j]
            num -= nums[i]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            remained = target - num
            if remained in seen:
                return [seen[remained], idx]
            else:
                seen[num] = idx # seen[2] = 0

