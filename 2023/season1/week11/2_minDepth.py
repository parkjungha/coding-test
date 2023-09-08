# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Runtime 56.40% (587ms) Memory 5.4% (57.2MB)
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right: # leaf node일 경우
            return 1
        if not root.left and root.right: # right child만 있을 경우
            return self.minDepth(root.right) + 1
        if root.left and not root.right: # left child만 있을 경우
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

# DFS보다 빠른 풀이 - BFS
class Solution:
    # Runtime 78.67% (528ms) Memory 72.21% (51MB)
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = deque([(root,1)]) # curr node, depth

        while q:
            cur, depth = q.popleft()
            if not cur.left and not cur.right: # leaf node에 도달한 경우 바로 반환 -> 오른쪽 왼쪽 관계없이 min인 것
                return depth
            
            # 너비우선탐색으로 왼쪽 오른쪽 존재하면 queue에 차례로 넣음 
            if cur.left:
                q.append((cur.left, depth+1))
            if cur.right:
                q.append((cur.right, depth+1))
