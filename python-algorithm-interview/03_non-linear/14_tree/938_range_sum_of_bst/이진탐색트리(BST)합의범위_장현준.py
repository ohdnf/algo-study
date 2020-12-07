# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
                
        if not root:
            return 0
        left = self.rangeSumBST(root.left, low, high)
        right = self.rangeSumBST(root.right, low, high)
        node = root.val if low <= root.val <= high else 0
        return left + right + node
'''
Runtime: 276 ms, faster than 15.31% of Python3 online submissions for Range Sum of BST.
Memory Usage: 22.3 MB, less than 17.58% of Python3 online submissions for Range Sum of BST.
'''