class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        def decode(num): # str to int
            ans = 0
            for n in num:
                ans += 10*ans + (ord(a)-ord('0'))

            return ans
        def encode(s): # int to str
            ans = ""
            while s > 0:
                t = s % 10
                s //= 10
                ans = chr(ord('0') + a) + ans
            return ans

        return encode(decode(num1)*decode(num2))

        def decode(num):
            ans = 0
            for i in num:
                ans = ans*10 +(ord(i) - ord('0'))
            return ans

        def encode(s):
            news = ''
            while s:
                a = s % 10
                s = s // 10
                news = chr(ord('0') + a) + news
            return news
        
        return encode(decode(num1)*decode(num2))
