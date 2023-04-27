# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # DFS 탐색 -> 재귀로 leaf 노드까지 찍고 돌아옴. 
    # Runtime 87.74% (38ms) Memory 46.96% (16.2MB)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root:
                return depth
                
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
            
        return dfs(root, 0)
    
    # BFS 탐색 -> Queue 사용
    # Runtime 62.75% (43ms) Memory 97.31% (15.2MB)
    # 다시 돌리니까 Runtime 90.38% (37ms) 나옴
    from collections import deque
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        
        depth = 0
        q = deque()
        q.append([root]) # 첫번째 root부터 넣어줌
        while q:
            for _ in range(len(q)): # 현재 queue에 
                root = q.popleft()
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            depth += 1
        return depth

'''
        initial: [3]
        1 iteration: [9, 20] d = 1
        2 iteration: [15, 7] d = 2
        3 iteration: [] d = 3 

'''