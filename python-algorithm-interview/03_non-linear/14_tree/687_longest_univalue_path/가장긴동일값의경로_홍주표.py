# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.max_len = 0

        def dfs(node):
            if not node:
                return 0, None

            left_len, left_val = dfs(node.left)
            right_len, right_val = dfs(node.right)

            lengths = [1]

            if left_val == node.val:
                lengths.append(left_len)

            if right_val == node.val:
                lengths.append(right_len)

            if len(lengths) == 3:
                curr_len = lengths[0] + max(lengths[1:])
                curr_max_len = sum(lengths)
            else:
                curr_len = curr_max_len = sum(lengths)

            self.max_len = max(self.max_len, curr_max_len)

            return curr_len, node.val

        dfs(root)

        if self.max_len:
            return self.max_len - 1
        else:
            return 0


"""
Runtime: 400 ms, faster than 54.34% of Python3 online submissions for Longest Univalue Path.
Memory Usage: 18.2 MB, less than 5.52% of Python3 online submissions for Longest Univalue Path.
"""

# leetcode solution
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.max_len = 0

        def length(node):
            if not node:
                return 0
            left_length = length(node.left)
            right_length = length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.max_len = max(self.max_len, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        length(root)

        return self.max_len