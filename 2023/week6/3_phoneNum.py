class Solution:
    # Run 12.51% Mem 98.22%
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        dic = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        cand = []
        for digit in digits:
            cand.append(dic[int(digit)])
        
        return list(map(''.join, list(product(*cand))))
    
    # Run 80.54% Mem 21.13%
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for j in dic[digits[i]]:
                backtrack(i+1, curStr + j)
        backtrack(0, "")

        return res
