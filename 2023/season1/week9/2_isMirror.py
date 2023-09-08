# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Run 67.83% (35ms) Mem 87.55% (13.9MB)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.isMirror(root.left, root.right)

    def isMirror(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val: 
            return False
        return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)