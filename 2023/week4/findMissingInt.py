class Solution:
    # Run 12.35% (358ms) Mem 7.7% (32.5MB)
    def firstMissingPositive(self, nums: List[int]) -> int:
        numSet, i = set(nums), 1
        while i in numSet:
            i += 1
        return i 

    # Run 9.34% (383ms) Mem 31.63% (27.7MB)

    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 in nums: 
            nums.sort()
            for i in range(len(nums)-1):
                if nums[i+1] != nums[i] + 1 and nums[i+1] != nums[i]:
                    if nums[i] + 1 > 0:
                        return nums[i] + 1
            return nums[len(nums)-1] + 1
            
        else: return 1