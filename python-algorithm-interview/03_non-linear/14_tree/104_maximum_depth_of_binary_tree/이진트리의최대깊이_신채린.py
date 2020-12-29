# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 데크 자료형을 사용하면 이중 연결 리스트로 구성되어 있기 때문에 
# 큐와 스택 연산을 모두 자유롭게 활용 가능할 뿐만 아니라 
# 양방향 모두 O(1)에 추출할 수 있어 좋은 성능을 보인다.
import collections 
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0
        while queue:
            depth += 1
            
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return depth 

# Runtime: 36 ms, faster than 89.27% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 15.3 MB, less than 84.17% of Python3 online submissions for Maximum Depth of Binary Tree.
# Next challenges: