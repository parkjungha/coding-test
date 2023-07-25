class Solution:
    # TLE (115 / 136)
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    s = words[i] + words[j]
                    if s == s[::-1]:
                        ans.append([i,j])

        return ans

class Solution:
    # Run 84.61% (1454ms) Mem 44.69% (29.6mb)
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []
        dic = {word[::-1]: idx for idx, word in enumerate(words)} # {reverse of words : index}

        for i, word in enumerate(words): # 모든 단어에 대해서 
            if "" in dic and dic[""] != i and word == word[::-1]: # emptry string이 있는 경우, 현재 단어가 palindrome이면 됨
                ans.append([i,dic[""]]) # idx 추가

            for j in range(1, len(word)+1): # 현재 단어의 모든 character 돌면서
                l = word[:j] # 왼쪽 substring
                r = word[j:] # 오른쪽 substring
                if l in dic and dic[l] != i and r == r[::-1]: # 왼쪽 substring이 dic에 있으면서 오른쪽 substring이 palindrome이면
                    ans.append([i,dic[l]])
                if r in dic and dic[r] != i and l == l[::-1]: 
                    ans.append([dic[r], i]) 
                
        return ans