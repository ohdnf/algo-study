# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0

        if root is None:
            return 0

        q = collections.deque()
        q.append((1, root))

        while q:
            depth, curr = q.popleft()
            if max_depth < depth:
                max_depth = depth

            if curr.left:
                q.append((depth + 1, curr.left))
            if curr.right:
                q.append((depth + 1, curr.right))

        return max_depth

"""
Runtime: 44 ms, faster than 37.54% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.3 MB, less than 82.11% of Python3 online submissions for Maximum Depth of Binary Tree.
"""