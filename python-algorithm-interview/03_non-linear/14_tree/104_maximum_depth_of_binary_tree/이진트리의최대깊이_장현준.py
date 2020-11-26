# BFS 이용한 깊이 depth를 측정
# 1. Q에 노드와 깊이를 같이 tuple로 함께 넣는 코드
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # left 나 right가 == None 이면 없는겨
        from collections import deque
        q = deque()
        maxDepth = 0
        if root == None:
            return 0
        else:
            q.append((root,1)) # TreeNode와 현재 깊이
        while q:
            # 1.TreeNode를 꺼낸다.
            now, depth = q.popleft()
            maxDepth = max(maxDepth, depth)
            # 2. TreeNode의 left 나 right의 값이 TreeNode이면 Q에 depth+1하면서 넣는다.
            if now.left != None:
                q.append((now.left, depth+1))
            if now.right != None:
                q.append((now.right, depth+1))
        return maxDepth
# Runtime: 36 ms, faster than 89.27% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 15.4 MB, less than 82.81% of Python3 online submissions for Maximum Depth of Binary Tree.

# 2. 책 코드, Q에 노드만 넣는다. len(Q)만큼 반복하는 코드를 통해 동일 레벨의 모든 노드를 순회한다. 이때 depth += 1 해준다.
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # left 나 right가 == None 이면 없는겨
        from collections import deque
        q = deque()
        depth = 0
        if root == None:
            return depth
        else:
            q.append(root) # TreeNode와 현재 깊이
        while q:
            # 1. 동일 레벨의 노드들을 모두 뽑는다. 이때 depth는 1개씩 증가시켜준다.
            depth += 1
            for _ in range(len(q)): 
                cur_root = q.popleft()
                # 자식 노드가 있으면 Q에 넣는다.
                if cur_root.left != None:
                    q.append(cur_root.left)
                if cur_root.right != None:
                    q.append(cur_root.right)
        return depth
# Runtime: 28 ms, faster than 99.49% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 15.4 MB, less than 82.37% of Python3 online submissions for Maximum Depth of Binary Tree.