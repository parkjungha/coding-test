# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Max Sum 선택할 때 네가지 경우중에 최대값 선택
# 1. root node만 
# 2. root node + right child nodes
# 3. root node + left child nodes 
# 4. root node + left child nodes + right child nodes

# 여기서 child nodes는 dfs로 재귀적으로 최대값 가져옴

class Solution:
    # Runtime 21.34% (99ms) Memory 5.95% (24.2MB)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -float("inf")

        def dfs(root):
            if not root:
                return 0

            leftSum = dfs(root.left)
            rightSum = dfs(root.right)
            leftPath = leftSum + root.val
            rightPath = rightSum + root.val

            self.maxSum = max(self.maxSum, root.val, leftPath, rightPath, leftPath + rightSum)
            return max(leftPath, rightPath, root.val) # 경로를 이어나가야 하므로 return 값은 왼쪽 오른쪽 자식 둘다 포함하는 경우는 불가능. 

        dfs(root)
        return self.maxSum