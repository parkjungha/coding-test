def lengthOfLongestSubstring(s: str) -> int: # Sliding Window 
    chars = set()
    max_length = 0
    i,j = 0,0
    while(j < len(s)):
        if s[j] not in chars:
            chars.add(s[j])
            j += 1
            max_length = max(max_length, j-i)
        else: # 반복되는 문자가 있을 때 시작점을 옮김
            chars.remove(s[i])
            i += 1
    return max_length

def lengthOfLongestSubstring(s: str) -> int: # Hashmap to keep track of the last seen index of each character in the input string 
    start = 0
    max_len = 0
    chars = {}
    for end in range(len(s)):
        if s[end] in chars:
            start = max(start, chars[s[end]]+1)
        chars[s[end]] = end
        max_len = max(max_len, end-start+1)
    return max_len
        