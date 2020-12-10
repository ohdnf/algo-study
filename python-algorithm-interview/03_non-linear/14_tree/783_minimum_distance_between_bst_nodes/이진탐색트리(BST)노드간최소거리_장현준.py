# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    minValue = float('inf')
    def minDiffInBST(self, root: TreeNode) -> int:
        def check(root: TreeNode) -> int:
            if not root: return float('inf')
            if root.right:
                node = root.right
                while node.left:
                    node = node.left
                dr = node.val - root.val
            else:
                dr = float('inf')
            if root.left:
                node = root.left
                while node.right:
                    node = node.right
                dl = root.val - node.val
            else:
                dl = float('inf')
            return min(dr, dl)
        if not root: return float('inf')
        return min(check(root), self.minDiffInBST(root.left), self.minDiffInBST(root.right))
'''
Runtime: 36 ms, faster than 15.33% of Python3 online submissions for Minimum Distance Between BST Nodes.
Memory Usage: 14.4 MB, less than 10.98% of Python3 online submissions for Minimum Distance Between BST Nodes.
'''