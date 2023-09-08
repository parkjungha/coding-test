class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        left = 0
        d = defaultdict(int)
        
        for right, char in enumerate(s):
            if right == 0: # 맨 처음 초기화
                d[char] = 1 # 첫번째 글자
                prev = char # 이전 글자 정보 저장
                continue
            
            # 이전 글자랑 현재 글자 비교해서 연속된 문자가 아니면, left pointer 땡겨줌
            if (ord(char) - ord(prev) != 1) and (ord(prev) - ord(char) != 25): # 연속된 글자인 경우 & za 인 경우 
                left = right

            d[char] = max(d[char], right - left + 1) # 연속된 문자가 아니면 right - left + 1 값이 1이 됨
            prev = char

        return sum(d.values())
            