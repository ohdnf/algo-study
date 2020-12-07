# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def makeNode(root: TreeNode, parent_val=0):
            
            if not root: return parent_val, None

            node = TreeNode(root.val)

            right_val, node.right = makeNode(root.right, parent_val)
            node.val += right_val
            left_val, node.left = makeNode(root.left, node.val)
            return left_val, node
        
        val, nodes = makeNode(root)
        return nodes

'''
Runtime: 32 ms, faster than 56.87% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
Memory Usage: 14.3 MB, less than 19.39% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
'''