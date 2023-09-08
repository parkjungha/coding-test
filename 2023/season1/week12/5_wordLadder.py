class Solution:
    # 시간초과 TC 32 / 36 .. 흠
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList: return []

        neighbors = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList: # 모든 단어들에 대해서 
            for i in range(len(word)): # 단어의 각 문자에 대해서
                pattern = word[:i] + "*" + word[i+1:] # replace each character in word with "*"
                neighbors[pattern].append(word)

        # BFS 
        visited = set([beginWord])
        q = deque()
        q.append((beginWord, [beginWord])) # (current word, path)
        ans = []
        wordList = set(wordList) # 중복 제거

        while q:
            for i in range(len(q)):
                word, seq = q.popleft()
                if word == endWord: # target word와 일치
                    ans.append(seq) 

                for i in range(len(word)): # 일치 X
                    pattern = word[:i] + "*" + word[i+1:]
                    for cand in neighbors[pattern]: # 가능한 neighbor
                        if cand in wordList: # wordlist에 존재하면
                            visited.add(cand)
                            q.append((cand, seq+[cand]))
            wordList -= visited
            
        return ans

# wordList = ["hot","dot","dog","lot","log","cog"]
# beginWord = 'hit', endWord = 'cog'

def bfs(beginWord, endWord, wordList):
    # create the adjacency list
    graph = defaultdict(list)                  
    for word in wordList: # "hot"
        for i in range(len(word)): 
            pattern = word[:i] + '.' + word[i+1:] # .ot - h.t - ho.
            graph[pattern].append(word) # graph[.ot] = [hot, dot, lot]

    q = deque([beginWord]) # path starting from beginWord

    # create a globaly visited key;value = node: [node how you got there] (like a parents list)
    all_visited = defaultdict(list)
    found_end = False

    while q and not found_end:
        visited_this_level = defaultdict(list)
        for _ in range(len(q)):     # go through each depth so you can accommodate other nodes that reach the end in the same level
            curNode = q.popleft()
            if curNode == endWord:                      # terminal condition: target word에 도달했을 때   
                found_end == True                        
            else: 
                for i in range(len(curNode)): 
                    curNodePattern = curNode[:i] + '.' + curNode[i+1:] # .it - h.t - hi.

                    for nextNode in graph[curNodePattern]: # 현재 단어에서 가능한 다음 단어들 모두 
                        if nextNode not in all_visited: 
                            if nextNode not in visited_this_level: # 아직 사용되지 않은 노드이면
                                q.append(nextNode)        
                            visited_this_level[nextNode].append(curNode)
        all_visited.update(visited_this_level)
    return all_visited

def dfs(beginWord, endWord, wordTree):
    if beginWord == endWord: 
        return [[beginWord]]
    if endWord not in wordTree:
        return []
    res = []
    parents = wordTree[endWord]
    for parent in parents:
        res += dfs(beginWord, parent, wordTree)
    for partialRes in res: 
        partialRes.append(endWord)
    return res

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):

        wordTree = bfs(beginWord, endWord, wordList)
        res = dfs(beginWord, endWord, wordTree)
        return res

