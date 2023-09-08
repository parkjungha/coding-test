class Solution:
    # 이진탐색
    # Runtime 49.11% (42ms) Memory 43.8% (13.8MB)
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid*mid == x:
                return mid
            if mid*mid > x:
                right = mid -1
            else:
                left = mid + 1
        return right

