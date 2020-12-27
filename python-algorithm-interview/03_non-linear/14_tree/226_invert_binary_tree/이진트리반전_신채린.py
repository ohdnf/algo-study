class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return None
            node.left, node.right = dfs(node.right), dfs(node.left)
            return node   
        return dfs(root)