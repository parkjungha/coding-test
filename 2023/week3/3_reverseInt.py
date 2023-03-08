
# Runtime 97.39% Memory 54.6%

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x <0 else 1
        val = int(str(abs(x))[::-1])
        if val > 2**31-1:
            return 0        
        return val*sign

# String 안쓰고 정석
    def reverse(self, x: int) -> int:
        reversed= 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            reversed = reversed*10 + x % 10
            x = x // 10 
        
        if reversed > (2**31 - 1):
            return 0
            
        return sign*reversed 

