class Solution:
    # Runtime 77.13%, Memory 99.28%
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len) # 제일 짧은 문자열 찾기
        
        for idx, char in enumerate(shortest): # 걔를 기준으로 idx랑 character하나씩 보면서
            for s in strs: # 다른 문자열에 대해 확인
                if s[idx] != char: 
                    return shortest[:idx]

        return shortest

    # Python zip 함수 
    # Runtime 94.93%, Memory 81.1%
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        res = ""
        for a in zip(*strs): # strs에서 원소 하나씩 빼서 tuple로 반환
            if len(set(a)) == 1: # 다 같은 글자일때
                res += a[0] # common prefix 
            else:
                return res
        return res 

    # String 정렬 (lexicographic order)을 이용
    # Runtime 65.87%, Memory 40.34%
    def longestCommonPrefix3(self, strs: List[str]) -> str:
        strs.sort()
        s1 = strs[0] # 처음
        s2 = strs[-1] # 마지막
        res = ""

        for i in range(len(s1)):
            if s1[i] == s2[i]: # 처음과 마지막의 prefix가 같으면 중간은 다 같은거
                res += s1[i]
            else: # 틀리면 X
                break
        return res