from collections import Counter

class Solution:
    # Run 75.99% (122ms) Mem 26.58% (14.8MB)

    def minWindow(self, s: str, t: str) -> str:
        t_map = Counter(t)
        char_needed = len(t_map) # t의 unique character개수
        left, right = 0, 0 # two pointer
        min_start = 0 # starting position
        min_len = float('inf') # length of the min window substring
        window_map = {} # current window 정보

        while right < len(s): # end pointer가 s 처음부터 끝까지 돌면서 
            char = s[right] # current char
            if char in t_map: # t에 있으면
                if char in window_map: # 이미 현재 윈도우에 포함되어있으면 +1
                    window_map[char] += 1
                else:
                    window_map[char] = 1

                # 현재 윈도우에 있는 개수랑 t에 있는 개수랑 같다면 matching된 것
                if window_map[char] == t_map[char]:
                    char_needed -= 1
                
            while char_needed == 0: # t의 모든 글자가 매칭되었다면, start pointer를 가능한 뒤로 조정
                if right - left + 1 < min_len: # 현재 window가 더 작다면 min window 업데이트
                    min_len = right - left + 1
                    min_start = left

                char = s[left] # 현재 start pointer가 있는 곳
                if char in t_map: # t에 있는 글자라면 
                    window_map[char] -= 1 # 현재 윈도우에서 하나 빼봄
                    if window_map[char] < t_map[char]: # 뺐는데 matching이 안되면
                        char_needed += 1 # chars 다시 하나 추가
                left += 1

            right += 1

        if min_len == float('inf'): return ""
        else: return s[min_start: min_start+min_len]