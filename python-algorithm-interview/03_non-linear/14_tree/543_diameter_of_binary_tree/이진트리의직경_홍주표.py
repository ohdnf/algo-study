# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        if root is None:
            return 0

        self.max_path = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.max_path = max(self.max_path, left + right)
            return max(left, right) + 1

        dfs(root)

        return self.max_path


"""
Runtime: 48 ms, faster than 34.82% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 16.5 MB, less than 19.95% of Python3 online submissions for Diameter of Binary Tree.
"""