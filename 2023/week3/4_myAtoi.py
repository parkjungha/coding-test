class Solution:
    def myAtoi(self, s: str) -> int:
        res = ""
        s = s.strip()
        sign = 1
        if not s: return 0
        
        if s[0] == "+":
            sign = 1
            s = s[1:]
        elif s[0] == "-":
            sign = -1
            s = s[1:]

        for i in s:
            if i.isdigit():
                res += i
            else:
                break

        if res == "": return 0 
        elif int(res)*sign > 2**31 -1: return 2**31 - 1
        elif int(res)*sign < -2**31: return -2**31
        return int(res)*sign 
