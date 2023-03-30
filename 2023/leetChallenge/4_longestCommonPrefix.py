class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key = len)
        for i in range(len(shortest)):
            for s in strs:
                if s[i] != shortest[i]:
                    return shortest[:i]

        return shortest

    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        res = ""
        for i in range(len(first)):
            if first[i] != last[i]:
                return first[:i]
            else:
                res += first[i]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for s in zip(*strs):
            if len(set(s)) == 1:
                res += s[0]
        return res