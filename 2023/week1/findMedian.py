class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        index = (len(nums) - 1) // 2
        return ((nums[index] + nums[~index]) / 2)

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        
        imin, imax, half_len = 0, m, (m+n+1) // 2
        while imin <= imax:
            i = (imin+imax) // 2 # Calculate the partition point in nums1
            j = half_len - i # Calculate the corresponding partion point in nums2
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
