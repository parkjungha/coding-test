class Solution:
    # Runtime 24.32% (431ms) Memory 67.78% (16.5MB)
    def shortestPalindrome(self, s: str) -> str:
        if s==s[::-1]: return s # 이미 Palindrome인 경우

        for i in range(len(s),-1,-1): # 뒤에서부터 한글자씩 빼면서 Palindrome인지 확인
            if s[:i] == s[:i][::-1]: # Palindrome이면
                added = s[i:][::-1] # 앞에 추가되어야 함
                break
        return added + s