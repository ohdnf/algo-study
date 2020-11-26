class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def madeNode(node: TreeNode) -> TreeNode:
            if node == None:
                return None
            return TreeNode(node.val, madeNode(node.right), madeNode(node.left))    
        return madeNode(root)
# Runtime: 48 ms, faster than 5.43% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 14.3 MB, less than 7.55% of Python3 online submissions for Invert Binary Tree.