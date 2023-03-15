class Solution:
    def myAtoi(self, s: str) -> int:
        res = ""
        s = s.strip() # whitespace 제거 
        sign = 1
        if not s: return 0
        
        # + - 부호 처리
        if s[0] == "+":
            sign = 1
            s = s[1:]
        elif s[0] == "-":
            sign = -1
            s = s[1:]

        # digit만 추출
        for i in s:
            if i.isdigit():
                res += i
            else:
                break

        if res == "": return 0 # If no digits, return 0
        elif int(res)*sign > 2**31 -1: return 2**31 - 1 # greater than max limit
        elif int(res)*sign < -2**31: return -2**31 # less than min limit
        return int(res)*sign # final result 
