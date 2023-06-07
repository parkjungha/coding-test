class Solution:
    # 문자열의 효율적인 탐색과 저장을 위해 Trie 사용
    # 그래프 탐색을 위해 DFS 사용

    # Runtime 80.52% (1013ms) Memory 60.38% (18.2MB)
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(x,y,root):
            letter = board[x][y] 
            cur = root[letter] # 자식 노드
            word = cur.pop('#', False) # 현재 글자로 끝나는 단어가 있으면 pop해서 해당 단어전체 반환. 없으면 False 반환
            if word: # valid word가 있으면 
                res.append(word) # result에 추가 

            board[x][y] = '*' # 현재 칸 방문 표시

            dx = [-1,1,0,0]
            dy = [0,0,-1,1]
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<m and 0<=ny<n and board[nx][ny] in cur: # 인접한 칸에 대해서 매칭되는 글자가 있으면
                    dfs(nx,ny,cur) # Recursively 탐색

            board[x][y] = letter # Backtracking: 원래 값으로 돌려줌
            if not cur: # 더이상 자식이 없으면 제거 
                root.pop(letter)

        # Build the trie from the list of words  
        trie = {}
        for word in words: # oath
            cur = trie # cur = {}
            for letter in word: # o a t h 
                cur = cur.setdefault(letter, {}) # 
            cur['#'] = word # 문자열의 종료를 알리는 flag
        

        m, n = len(board), len(board[0])
        res = []

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie: # 현재 글자로 시작하는 단어가 Trie에 있으면 
                    dfs(i,j,trie) # DFS 탐색
        
        return res
