# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        val = preorder[0] # 부모 노드 값
        node = TreeNode(val)
        i = inorder.index(val) # inorder의 부모 노드 값을 기준으로 L N R 나뉨         
        node.left = self.buildTree(preorder[1:1+i], inorder[:i])
        node.right = self.buildTree(preorder[1+i:], inorder[i+1:])
        return node
'''
Runtime: 196 ms, faster than 31.74% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 88.5 MB, less than 10.36% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
'''