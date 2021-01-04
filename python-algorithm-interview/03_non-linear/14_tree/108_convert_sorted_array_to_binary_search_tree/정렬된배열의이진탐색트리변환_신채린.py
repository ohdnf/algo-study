# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        # find middle 
        mid = len(nums) // 2
      
        # make the middle element the root 
        root = TreeNode(nums[mid]) 

        # left subtree of root has all 
        root.left = self.sortedArrayToBST(nums[:mid]) 

        # right subtree of root has all  
        root.right = self.sortedArrayToBST(nums[mid+1:]) 
        return root 
