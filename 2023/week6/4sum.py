class Solution:
    # Time Complexity : O(N^4) -> Time out
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        for a in range(len(nums)-3):
            for b in range(a+1, len(nums)-2):
                for c in range(b+1, len(nums)-1):
                    for d in range(c+1, len(nums)):
                        temp = sorted([nums[a], nums[b], nums[c], nums[d]])
                        if sum(temp) == target:
                            if temp not in res:
                                res.append(temp)
        return res
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
                return
            if N == 2: # Two pointer approach for 2-sum problem
                l,r = 0, len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l],nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else: # s > target:
                        r -= 1
            else: # N == 3, 4 면 recursively reduce N
                for i in range(len(nums)-N+1):
                    if i == 0 or (i>0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results
    
    def threeSum(self, nums, target):
        results = []
        nums.sort()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            t = target - nums[i]
            if i == 0 or nums[i] != nums[i-1]:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == t:
                        results.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]: l += 1
                        while l < r and nums[r] == nums[r-1]: r -= 1
                        l += 1,
                        r -= 1
                    elif s < t:
                        l += 1
                    else:
                        r -= 1
        return results

    def fourSum(self, nums, target):
        results = []
        nums.sort()
        for i in range(len(nums)-3):
            if i == 0 or nums[i] != nums[i-1]: 
                threeResult = self.threeSum(nums[i+1:], target-nums[i])
                for item in threeResult:
                    results.append([nums[i]] + item)
        return results 
        
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        