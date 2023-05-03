# DFS로 왼쪽 오른쪽 subtree 각각에 대해 끝까지 가면서 balanced인지 판별하기 
class Solution:
    # Runtime 58.35% (54ms) Memory 5% (21.2MB)
    def isBalanced(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return 0
            
            leftD = dfs(root.left) # left subtree의 height
            rightD = dfs(root.right) # right subtree의 height

            if abs(leftD-rightD) > 1: # height가 1 이상 차이나면
                return -1 

            if leftD == -1 or rightD == -1: # subtree가 balanced가 아니면
                return -1
            
            return 1 + max(leftD, rightD) # balanced한 경우, max height 반환
            
        return dfs(root) != -1 
