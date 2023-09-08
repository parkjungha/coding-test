# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # Runtime 91.18% (122ms) Memory 72.57% (22.3MB)
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        s = [] # string의 각 문자를 저장할 list
        
        def preorder(root):
            if not root:
                s.append('n') # 끝을 나타내기 위해서
                return
            s.append(str(root.val))
            preorder(root.left) # 왼쪽 먼저
            preorder(root.right)
        
        preorder(root)
        return ' '.join(s)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        q = deque(data.split())

        def preorder():
            s = q.popleft()
            if s == 'n':
                return None
            root = TreeNode(s) # creates a node
            root.left = preorder() # recursively constructs its left 
            root.right = preorder() # and right subtrees
            return root

        return preorder()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))