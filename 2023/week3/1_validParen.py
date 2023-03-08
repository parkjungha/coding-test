
# Runtime 78.52% Memory 97.37%

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(':')', '{':'}', '[':']'}
        for char in s:
            if char in dic.keys(): # open
                stack.append(char)
            else: # close
                if not stack or dic[stack.pop()] != char:
                    return False

        if stack:
            return False
        return True