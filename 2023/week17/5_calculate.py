class Solution:
    # Run 49.82% (104ms) Mem 56.1% (17.8MB)
    def calculate(self, s: str) -> int:
        ans = 0
        num = 0
        sign = 1
        stack = [sign]

        for ch in s:
            if ch.isdigit(): # 숫자이면
                num = num*10 + int(ch) # 현재 가지고 있는 숫자의 일의자리수로 더해줌
            elif ch == '(': 
                stack.append(sign)
            elif ch == ')': 
                stack.pop()
            elif ch == '+' or ch == '-':
                ans += sign*num
                sign = (1 if ch=='+' else -1) * stack[-1] # 현재 stack의 top 부호 반영해서 갱신
                num = 0 # 초기화
        
        return ans + sign*num