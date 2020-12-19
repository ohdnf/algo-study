# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.keys = []
        self.min_diff = 200

        def find_key(node):
            if node:
                find_key(node.left)
                for key in self.keys:
                    if self.min_diff > abs(key - node.val):
                        self.min_diff = abs(key - node.val)
                if self.min_diff == 1:
                    return
                self.keys.append(node.val)
                find_key(node.right)

        find_key(root)
        return self.min_diff

# Other solution
class Solution:
    prev = float('-inf')
    min_diff = float('inf')

    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.min_diff = min(self.min_diff, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.min_diff