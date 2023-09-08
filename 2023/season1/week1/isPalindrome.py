class Solution:
    def isPalindrome(self, x: int) -> bool: # String 으로 변경
        if x < 0: return False
        if str(x) == str(x)[::-1]: return True 

    def isPalindrome2(self, x: int) -> bool:
        if x < 0: return False
        newNum = 0
        while 0 < x:
            newNum = newNum*10 + x%10
            x = x//10
        return newNum == oldNum

    def isPalindrome3(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10 == 0): return False
        result = 0
        while x > result: 
            result = result*10 + x%10
            x = x//10
        return True if (x==result or x==result//10) else False
