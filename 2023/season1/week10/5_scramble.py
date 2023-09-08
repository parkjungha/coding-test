from functools import cache
# @cache 데코레이터를 함수 위에 선언하면, 함수에 넘어온 인자를 key로, 함수 호출 결과를 value로 메모이제이션이 적용됩니다.
# Python에서 Memoization을 사용할 때 @cache 또는 @lru_cache를 사용하면 이전 함수 호출 결과값을 dictionary에 보관해둠으로써 시간 초과 방지
class Solution:
    @cache 
    def isScramble(self, s1: str, s2: str) -> bool: # s2가 s1의 scrambled string인지 판별
        if s1 == s2:
            return True
        if Counter(s1) != Counter(s2): # 알파벳 개수, 구성이 다르면 바로 짤
            return False

        for i in range(1, len(s1)): # 모든 가능한 파티션에 대해서 쪼개보면서 
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):  
            # 둘다 swap 안하거나, 둘다 swap 한 경우 or 하나만 swap 한 경우
            # recursively on each of the two substrings    
                return True

        return False