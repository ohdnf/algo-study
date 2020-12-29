class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return None
            node.left, node.right = dfs(node.right), dfs(node.left)
            return node   
        return dfs(root)
# Runtime: 24 ms, faster than 95.03% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 14.2 MB, less than 56.46% of Python3 online submissions for Invert Binary Tree.



# BFS 방식
def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft() 
            
            if node:
                node.left, node.right = node.right, node.left 
                
                queue.append(node.left)
                queue.append(node.right)
        return root

# Runtime: 32 ms, faster than 56.74% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 14.3 MB, less than 29.68% of Python3 online submissions for Invert Binary Tree.

#DFS 방식
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])
        
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left 
                
                stack.append(node.left)
                stack.append(node.right)
        return root

Runtime: 28 ms, faster than 82.35% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14.2 MB, less than 56.46% of Python3 online submissions for Invert Binary Tree.