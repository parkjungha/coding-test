# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Runtime 41.19% (35ms) Memory 59.70% (13.9MB)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
                
        if not p or not q:
            return False

        if p.val != q.val: 
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)