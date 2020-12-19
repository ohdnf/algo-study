# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    acc: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        # 오른쪽에서 왼쪽으로 중위 순회하면서 값을 누적
        self.bstToGst(root.right)
        self.acc += root.val
        root.val = self.acc
        self.bstToGst(root.left)

        return root