# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        self.diff = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if self.diff < abs(left - right):
                self.diff = abs(left - right)

            return max(left, right) + 1

        dfs(root)

        if self.diff > 1:
            return False
        else:
            return True


"""
Runtime: 52 ms, faster than 59.60% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 19.3 MB, less than 6.48% of Python3 online submissions for Balanced Binary Tree.
"""


# solutions of discuss
# recursive
class Solution(object):
    def isBalanced(self, root):

        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1


# iterative
class Solution(object):
    def isBalanced(self, root):
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True
