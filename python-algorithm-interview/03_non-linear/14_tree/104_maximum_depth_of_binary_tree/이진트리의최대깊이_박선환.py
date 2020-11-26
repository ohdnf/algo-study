class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0
        if root == None:
            return max_depth
        
        from collections import deque
        dq = deque()
        dq.append((root, 1))
        
        while dq:
            current_node, depth = dq.popleft()
            if max_depth < depth:
                max_depth = depth
            if current_node.left != None:
                dq.append((current_node.left, depth + 1))
            if current_node.right != None:
                dq.append((current_node.right, depth + 1))
        return max_depth

# 11/26/2020 19:55	Accepted	44 ms	15.4 MB	python3