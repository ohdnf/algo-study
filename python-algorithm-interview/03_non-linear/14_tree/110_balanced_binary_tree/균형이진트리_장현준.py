# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        if root == None:
            return 1 # 리프노드에서 리턴받는 부모노드까지의 높이

        # if height == False: 논밸런스
        # if height != False: 밸런스, 값은 리프노드에서 현재노드까지의 높이
        left_height = self.isBalanced(root.left)
        right_height = self.isBalanced(root.right)

        # 아래 노드가 이미 논밸런스이거나, 현재 노드가 논밸런스이면 False 리턴
        if (not left_height or not right_height) or abs(left_height - right_height) >= 2:
            return False
        else:
            return max(left_height, right_height)+1 
''' 편차가 심함. 결과 수치에 큰 미련 가질 필요 없을듯
Runtime: 44 ms, faster than 91.49% of Python3 online submissions for Balanced Binary Tree.
Memory Usage: 18.3 MB, less than 48.92% of Python3 online submissions for Balanced Binary Tree.
'''