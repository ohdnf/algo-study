# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            
            return max(left, right) + 1
        dfs(root)
        return self.longest