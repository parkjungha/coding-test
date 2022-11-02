# Trie 자료구조: 문자열 검색에 주로 사용. 문자열을 트리 형식으로 저장하여 빠르게 검색함
# 트리의 깊이 = 단어의 길이

class Node(object):
    def __init__(self, key, cnt = 0):
        self.key = key
        self.cnt = cnt
        self.child = {}

class Trie():
    def __init__(self):
        self.head = Node(None) # 루트노드

    def insertTree(self, string):
        cur = self.head
        for token in string:
            if token not in cur.child:
                cur.child[token] = Node(token)
            cur = cur.child[token]
            cur.cnt += 1

    def searchTree(self, string):
        cur = self.head
        cnt = 0
        for token in string: # 한글자씩 돌면서 트리 순회 
            cnt += 1
            cur = cur.child[token] # 자식 노드 
            if cur.cnt == 1: # 1인 경우는 해당 노드에 한 번만 방문한 것, 즉 현재 단어 빼고는 해당 노드를 거치는 노드가 없다는 의미
                return cnt
        return len(string)
        # 해당 단어를 끝까지 탐색했음에도 카운트가 1인 노드를 만나지 못했다면, 해당 단어는 다른 단어의 접두사.
        # 따라서 해당 단어는 단어의 전부를 입력해야함

def solution(words):
    answer = 0
    wordTree = Trie()
    for word in words:
        wordTree.insertTree(word)
    for word in words:
        answer += wordTree.searchTree(word)

    return answer

####################################################################################
def make_trie(words):
    dic = {}
    for word in words:
        current_dict = dic
        for letter in word:
            current_dict.setdefault(letter, [0, {}]) # key값: default 로 설정할 value값
            current_dict[letter][0] += 1 # count++1
            current_dict = current_dict[letter][1] # 자식 노드로
    return dic
    
["go","gone","guild"]	
{'g': [3, {'o': [2, {'n': [1, {'e': [1, {}]}]}], 'u': [1, {'i': [1, {'l': [1, {'d': [1, {}]}]}]}]}]}



def solution(words):
    answer = 0
    trie = make_trie(words)
    for word in words:
        temp =trie
        for letter in word:
            answer += 1
            temp = temp[letter]
            if temp[0] == 1: 
                break
            else:
                temp = temp[1]
    return answer