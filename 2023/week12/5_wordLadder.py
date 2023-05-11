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

