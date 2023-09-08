# Runtime 96.39% (26 ms) Memory 97.27% (13.7 MB)

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) == (divisor < 0) 
        # 둘다 양수이거나, 둘다 음수이면 positive = True

        dividend, divisor = abs(dividend), abs(divisor)

        ans = 0

        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                ans += i
                i <<= 1 # 2 4 8 16 ...
                temp <<= 1 # 2*divisor

        if not positive:
            ans = (-1)*ans

        return min(max(-2**31, ans), 2**31-1)
 
