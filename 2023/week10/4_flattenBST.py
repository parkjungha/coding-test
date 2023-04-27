# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 이진트리 전위순회 root -> 왼 -> 오
    # DFS로 왼쪽부터 leaf까지 들어갔다가 오른쪽 ... 
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        self.cur = None # 이전 값 Pointer 역할
        
        def dfs(node):
            if not node:
                return

            left, right = node.left, node.right
            node.left = None # 왼쪽은 null

            if self.cur:
                self.cur.right = node # 앞에서 사용한 pointer의 오른쪽이 현재 node를 가르키도록
                self.cur = self.cur.right # Pointer 업데이트 (현재 가장 오른쪽 자식 노드)
            
            else: # Initialize - root로 
                self.cur = node

            dfs(left) #
            dfs(right)
        
        dfs(root)
        
# dfs(1), left=2, right=5, 1.left = None, cur = 1, 
# dfs(2), left=3, right=4, 2.left = None, 1.right = 2, cur = 2
# dfs(3), left=None, right=None, 3.left = None, 2.right = 3, cur = 3
# dfs(None) return
# dfs(None) return
# dfs(4), left=None, right=None, 4.left = None, 3.right = 4, cur = 4
# dfs(None) return
# dfs(None) return
# dfs(5), left=None, right=6, 5.left = None, 4.right = 5, cur = 5
# dfs(None) return
# dfs(6), left=None, right=None, 6.left = None, 5.right = 6, cur = 6
# dfs(None) return
# dfs(None) return
