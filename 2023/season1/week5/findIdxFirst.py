class Solution:
    # Runtime 74.99% (30ms) Memory 53.82% (13.8MB)
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    # Runtime 70.18% (31ms) Memory 95.13% (13.8MB)
    # find 직접 구현
    def strStr(self, haystack: str, needle: str) -> int:
        for idx in range(len(haystack)-len(needle)+1):
            if haystack[idx:idx+len(needle)] == needle: # 문자열 슬라이싱
                return idx
        return -1
