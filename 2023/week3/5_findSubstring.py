from itertools import permutations

class Solution:
# Trial1: permutation으로 가능한 조합 전부 만들어놓고 하나씩 일치하는지 검사 -> 당연히 시간초과 하하
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        length = len(words[0])
        numOfWords = len(words)
        substr_len = numOfWords * length
        if len(s) < length*numOfWords: return []

        answer = []
        candidates = list(map(''.join, permutations(words, numOfWords)))
        
        for i in range(len(s)): 
            split = s[i : i + substr_len] # substring 길이 단위로 자름
            if split in candidates:
                answer.append(i)

        return answer

# Trial 2: Counter 이용해서 비교 
# Runtime 28.76%, Memory 69.8%
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        numOfWords = len(words)
        length = len(words[0])
        substr_len = numOfWords * length
        answer = []
        counter = Counter(words)

        for i in range(len(s) - substr_len + 1):
            temp = s[i : i + substr_len] # substring 길이 단위로 자름
            lst = []
            while temp: 
                lst.append(temp[:length]) # temp를 word 길이 단위로 잘라서 lst에 넣음
                temp = temp[length:]
            if Counter(lst) == counter:
                answer.append(i)
        
        return answer

# Runtime 80.49%, Memory 97.89%
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        numOfWords = len(words)
        length = len(words[0])
        substr_len = numOfWords * length
        answer = []

        # left: start character position
        for left in range(length):
            counter = Counter(words)

            # move 'right'
            for right in range(left, len(s) - length + 1, length):
                word = s[right : right + length]
                counter[word] -= 1 # counter 내의 단어들의 값이 모두 한번씩 쓰여져서 0 이 될때가 정답 

                while counter[word] < 0: # 음수가 되면 불필요한 단어가 있다는 의미 -> left 이동해줌 
                    counter[s[left : left + length]] += 1
                    left += length
                if left + substr_len == right + length: # left와 right간의 거리가 substring 의 길이와 같아지면
                    answer.append(left) # answer 에 추가 

        return answer

