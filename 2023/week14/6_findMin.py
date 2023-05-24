class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Run 81.15% (53 ms)
        return min(list(set(nums)))

    # 이진탐색 (65 ms) 엥ㅎ
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) -1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]
            