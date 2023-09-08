# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Balanced binary search tree 만들기 
    # 정렬된 array에서 중앙 값 뽑아서 root가 되고, root를 기준으로 왼쪽 오른쪽 subtree recursive하게 반복
    # Run 33.26% (66ms) Mem 98.50% (15.4MB)
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root