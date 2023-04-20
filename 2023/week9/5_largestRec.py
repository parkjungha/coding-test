class Solution:
    # Monotonic stack: 스택의 원소들을 오름차순, 혹은 내림차순 상태를 유지하도록 하는 것
    def largestRectangleArea(self, bars: List[int]) -> int:
        stack = []
        ans = 0

        for bar in bars+[0]: # 맨 마지막 bar 고려해주기 위해서 하나 추가 (ex: [2,4]->4) 
            pops = 0
            while stack and stack[-1][1] >= bar: # stack의 마지막 원소의 height과 현재 bar의 height 비교
                width, height = stack.pop()
                pops += width
                ans = max(ans, pops*height)

            stack.append([pops+1, bar])
        
        return ans