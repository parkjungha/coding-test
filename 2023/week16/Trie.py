class Node(object):
    def __init__(self, key, data=None):
        self.key = key # 현재 글자 (character)
        self.data = data # 문자열의 끝을 나타내는 Flag
        self.children = {} # 자식 노드 

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    # 문자열 삽입
    def insert(self, string):
        curr_node = self.head
        # 삽입할 string의 각 문자에 대해 자식 Node를 만들며 내려간다.
        for char in string:
            # 자식 Node중 같은 문자가 없으면 Node 새로 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            # 같은 문자가 있으면 해당 자식 Node로 이동
            curr_node = curr_node.children[char]
        # 문자열이 끝난 지점의 노드의 data 값에 해당 문자열 입력
        curr_node.data = string 

    def search(self, string):
        # 가장 아래 노드부터 탐색 시작
        curr_node = self.head
        for char in string:
            # 현재 글자가 자식 Node에 있으면 해당 자식 Node로 이동
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        # 모든 글자에 대해 탐색이 끝난 후 현재 노드의 data에 값이 존재한다면
        # 문자가 포함되어 있다는 뜻
        if curr_node.data != None:
            return True

    