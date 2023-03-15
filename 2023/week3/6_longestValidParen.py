class Solution:
    # Stack: Space O(len(s))
    # Runtime 90.48% Memory 42.19%
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stack = [-1] # 초기화 시작 인덱스를 -1로 !!
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i) # index를 추가
            else: # ')' 이면 valid한지 판단
                stack.pop()
                if not stack: # stack이 비어있으면(-1가 사라지면): not valid. 현재 인덱스부터 탐색 새로 시작
                    stack.append(i)
                else: # 비어있지 않으면 (-1가 남아있으면) valid.
                    max_length = max(max_length, i-stack[-1]) # 최대 길이 갱신 (현재위치 + 1)
        return max_length
    
    # Two pointer: Space O(1)
    # Runtime 67.88% Memory 98.68%
    # "(()" 같은 경우를 위해서 양쪽에서 두번 돌아야함. 시간 복잡도 down
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        l,r = 0,0
        
        # 왼쪽에서 오른쪽으로 탐색
        for i in range(len(s)):
            if s[i] == '(':
                l += 1
            else: # ')'
                r += 1
            if l == r: # valid
                max_length = max(max_length, l+r) # 갱신
            elif r > l: # invalid
                l = r = 0 # 초기화

        l,r = 0,0
        # 오른쪽에서 왼쪽으로 탐색
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                l += 1
            else: # ')'
                r += 1
            if l == r: # valid
                max_length = max(max_length, l+r) # 갱신
            elif l > r: # invalid
                l = r = 0 # 초기화
        
        return max_length