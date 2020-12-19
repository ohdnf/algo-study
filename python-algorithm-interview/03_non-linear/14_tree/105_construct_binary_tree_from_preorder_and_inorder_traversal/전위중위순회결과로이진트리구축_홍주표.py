# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            index = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])

            return node


# 실패하는 코드
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        index = 1
        queue = collections.deque()
        queue.append(root)

        while index < len(preorder) and queue:
            curr = queue.popleft()
            curr_inx = inorder.index(curr.val)
            if inorder.index(preorder[index]) < curr_inx:
                curr.left = TreeNode(preorder[index])
                queue.append(curr.left)
                index += 1
            if curr_inx < inorder.index(preorder[index]):
                curr.right = TreeNode(preorder[index])
                queue.append(curr.right)
                index += 1

        return root