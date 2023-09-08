class Solution:
    # Runtime 73.71% (30ms) Memory 71.1% (13.8MB)
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    
    # Runtime 88.8% (27ms) Memory 29.4% (13.9MB)
    def lengthOfLastWord(self, s: str) -> int:
        leng = 0
        for i in range(len(s)-1, -1, -1): # 뒤에서부터
            if s[i] != " ":
                leng += 1
            elif s[i] == " " and leng > 0:
                return leng
        return leng