# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def switch(node):
            if not node:
                return

            node.left, node.right = switch(node.right), switch(node.left)
            return node

        return switch(root)


"""
Runtime: 24 ms, faster than 94.44% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14.3 MB, less than 7.55% of Python3 online submissions for Invert Binary Tree.
"""