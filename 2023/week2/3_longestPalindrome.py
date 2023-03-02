# Runtime 86.48% Memory 86.41%

def longestPalindrome(self, s: str) -> str:
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def isPalindrome(s, l, r):
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1
        return s[l+1:r]

    if len(s) < 2:
        return s

    ans = ""
    for i in range(len(s)):
        odd = self.isPalindrome(s,i,i)
        even = self.isPalindrome(s,i,i+1)
        if len(odd) > len(ans):
            ans = odd
        if len(even) > len(ans):
            ans = even
    return ans 

