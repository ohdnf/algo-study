# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.total = 0
        def dfs(n):
            if n:
                dfs(n.right)
                n.val     += self.total
                self.total = n.val
                dfs(n.left)
        dfs(root)
        return root