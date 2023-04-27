class Solution:
    # Run 35.64% (47ms) Mem 58.28% (13.9MB)
    def nextPermutation(self, nums: List[int]) -> None:
        i = j = len(nums) - 1

        while i>0 and nums[i-1] >= nums[i]: # 뒤에서부터 처음으로 오름차순이 아닌 값의 index 찾기
            i -= 1
        
        if i == 0:
            # 정렬되어 있는 경우
            nums.reverse()
            return
        
        while nums[j] <= nums[i-1]: # 뒤에서부터 nums[i-1]보다 큰 수의 index 찾기
            j -= 1
        
        nums[i-1], nums[j] = nums[j], nums[i-1] # i랑 j swap
        nums[i:] = nums[len(nums)-1 : i-1 : -1] # i부터 끝까지 reverse
