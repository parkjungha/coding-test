class Solution:
    # Return the minimum number of patches required to make [1,n]
    # Run 77ms (55.5%) Mem 16.39MB (93.43%)
    def minPatches(self, nums: List[int], n: int) -> int:
        i = 0 # index of the next number that we need to consider adding to the array.
        miss = 1 # smallest sum in [0,n]
        ans = 0 # number of patches

        while miss <= n: # 1부터 n까지
            if i < len(num) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else: # add patch number
                miss *= 2 # 표현할 수 있는 수 두배로 증가 
                patches += 1
            
        return patches