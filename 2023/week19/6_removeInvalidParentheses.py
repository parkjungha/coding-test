class Solution:
    # Run 63.17% (186ms) Memory 40.85% (16.6MB)
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # define when a combination of parenthesis is still valid
        def valid(candidate): # Balanced 한지 판별
            counter = 0
            for char in candidate:
                if char == "(": counter += 1
                elif char == ")": counter -= 1
                if counter < 0: 
                    return False
            return counter == 0

        # BFS
        candidates = set([s]) # s = "(a)())()"
        ans = set()
        while not ans: # ans가 생기면 바로 탐색 중단 (minimum of removals이기 때문)
            next = set() 
            for candidate in candidates: 
                if valid(candidate): 
                    ans.add(candidate)
                    continue
                
                # 하나씩 제거하면서 candidates 더 생성 
                for idx, ch in enumerate(candidate):
                    if ch not in "()": 
                        continue
                    next.add(candidate[:idx] + candidate[idx+1:]) # 해당 문자를 제거했을 때의 문자열 만들기
            candidates = next

        return ans