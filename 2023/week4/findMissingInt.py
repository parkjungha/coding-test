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

    # 정렬하면 무조건 time complexity가 O(nlogn) 이구나...
    # Run 11.54% Mem 7.1%
    def firstMissingPositive(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num > 0:
                dic[num] = num
        
        for i in range(1,len(dic)+1):
            if i not in dic:
                return i
        return len(dic)+1