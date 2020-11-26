# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def mergeNode(t1: TreeNode, t: TreeNode) -> TreeNode:
            if t1 == None and t == None:
                return None

            # val, left, right
            if t1 == None:
                val = t.val
                left = mergeNode(t.left, None)
                right = mergeNode(t.right, None)
            elif t == None:
                val = t1.val
                left = mergeNode(t1.left, None)
                right = mergeNode(t1.right, None)
            else:
                val = t1.val + t.val
                left = mergeNode(t1.left, t.left)
                right = mergeNode(t1.right, t.right)
            return TreeNode(val, left, right)
    
        return mergeNode(t1, t2)

# Runtime: 100 ms, faster than 14.37% of Python3 online submissions for Merge Two Binary Trees.
# Memory Usage: 16 MB, less than 6.18% of Python3 online submissions for Merge Two Binary Trees.