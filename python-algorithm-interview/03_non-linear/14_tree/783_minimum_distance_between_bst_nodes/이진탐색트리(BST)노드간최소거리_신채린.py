# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root :
            return 0
        def inorder(root) :
            if root.left :
                inorder(root.left)
            ans.append(root.val)
            if root.right :
                inorder(root.right)
        ans=[]
        inorder(root)
        last=float("inf")
        for i in range(len(ans)-1) :
            last=min(last,ans[i+1]-ans[i])
        return last
        