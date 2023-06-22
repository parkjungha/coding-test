class Solution:
    # count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

    # 시간초과 TC 35 / 38
    def countDigitOne(self, n: int) -> int:
        cnt = 0
        for i in range(n+1):
            cnt += str(i).count('1')

        return cnt 

    # Digit by Digit
    def countDigitOne(self, n: int) -> int:
        # 한자리수: 1 하나
        # 두자리수: 10~19 11개 + 8개: 19개
        # 세자리수 ... 
        cnt = 0
        place = 1 # 1, 10, 100, 1000, ... 10의 거듭제곱
        while place <= n: # Ex) n = 1234, place = 100 일때
            prefix = n // (place*10) # prefix = 1234 // (1000)  = 1
            digit = (n-prefix*(place*10)) // place # digit = 2
            suffix = n % place # suffix = 34

            cnt += prefix * place

            if digit > 1:
                cnt += place
            elif digit == 1:
                cnt += suffix+1
            place *= 10

        return cnt

# https://leetcode.com/problems/number-of-digit-one/solutions/3394934/easier-to-understand-solution-in-python/ 풀이 참고