# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS Run 13.94% (56ms) Mem 5.4% (17.6MB)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return 0
        q = deque([(root, root.val)])
        ans = []
        while q:
            cur, curVal = q.popleft()
            if not cur.left and not cur.right: # Leaf node
                ans.append(curVal)
            
            if cur.left:
                q.append((cur.left, cur.left.val + curVal))
            if cur.right:
                q.append((cur.right, cur.right.val + curVal))

        if targetSum in ans: return True
        else: return False

    # DFS Run 15.77% (55ms) Mem 5.4% (17.7MB)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, sumVal):
            if not root: return 0
            
            sumVal += root.val
            
            if not root.left and not root.right: # leaf node이면
                return sumVal == targetSum

            return dfs(root.left, sumVal) or dfs(root.right, sumVal) # 한번이라도 True 면 True 
        return dfs(root, 0)
