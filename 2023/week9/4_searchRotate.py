class Solution:
    # Linear Search O(n)
    # Run 14.21% (50ms) Mem 44.57% (14.2 MB)
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return nums.index(nums[i])
                break
        else:
            return -1

class Solution:
    # Binary Search 두번 O(logn)
    # Run 84.55% (39ms) Mem 10.87% (14.3 MB)
    def search(self, nums: List[int], target: int) -> int:
        # 피벗 포인트 찾기
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left
    
    # Target의 index 찾기
        if target >= nums[pivot] and target <= nums[-1]:
            left, right = pivot, len(nums) - 1
        else:
            left, right = 0, pivot - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
