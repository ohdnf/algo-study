# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return 0
            
            # leaf node까지 끝까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            
            #현재 node가 자식 노드와 동일한 경우 거리 1 증가 
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            
            # 왼쪽 & 오른쪽 자식 노드 간 거리의 합 최대값이 결과 
            self.result = max(self.result, left + right)
            # 자식 노드 상태값 중 가장 큰 값 리턴한다.
            return max(left, right)
        dfs(root) 
        return self.result 