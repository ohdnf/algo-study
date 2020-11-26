class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        from collections import deque
        leafNodes = deque()
        q = deque()
        if root == None or (root.left == None and root.right == None): # 자꾸 이상한 테케 주네 ㅡㅡ;;
            return 0
        else:
            q.append((root,[])) # 노드, 족보
        longest = -1 # (최고레벨-1) == root노드에서 가장 멀리 떨어진 leafNode와의 거리
        while q:
            longest += 1 # 레벨+1
            for _ in range(len(q)):
                cur_root, jokbo = q.popleft()
                if cur_root.left == None and cur_root.right == None:
                    leafNodes.append(jokbo)
                else:
                    if cur_root.left != None:
                        q.append((cur_root.left, jokbo+[-1]))
                    if cur_root.right != None:
                        q.append((cur_root.right, jokbo+[1]))
        # 공통 조상 찾기.
        for i in range(len(leafNodes)-1):
            for j in range(i+1, len(leafNodes)):
                commonParentLevel = 0 # 루트노드는 무조건 공통 조상 => commonParentLevel은 0이상!
                n1, n2 = leafNodes[i], leafNodes[j] # 변수 햇갈리지 않도록 선언
                commonDepth = min(len(n1), len(n2)) # 둘 중 작은 깊이까지만 공통 조상을 찾을만한 범위
                for level in range(commonDepth):
                    if n1[level] == n2[level]:
                        commonParentLevel += 1
                    else:
                        break
                longest = max(longest, len(n1)+len(n2)-2*commonParentLevel)
        return longest
# Runtime: 1172 ms, faster than 5.33% of Python3 online submissions for Diameter of Binary Tree.
# Memory Usage: 15.7 MB, less than 95.19% of Python3 online submissions for Diameter of Binary Tree.

# 뭔지 모르겠다
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 1. 부모노드에게 자식노드가 있다는것은 무슨 의미 일까...?
        # 1-1. 자식노드가 없다는것.
            # [] or [0] (root조차 없거나, root만 잇는 노드) => 정답은 0
        # 1-2. 자식노드가 있다?
            # 부모-자식간 => 길이: 1, 자식2 => 자식간 길이: 2
        # 2. left + right로 하면 어떨까? => 뭔가 이상쓰.
        # 2-1. left 와 right는 해당 편향이진트리 깊이? => 아니였다... ㅡㅡ

        maxValue = [0];
        def myNode(node, maxValue):
            if node == None:
                return {
                    "left": 0,
                    "right": 0,
                    "long": 0
                }
            leftNode = myNode(node.left, maxValue)
            rightNode = myNode(node.right, maxValue)
            left = leftNode["left"]
            right = rightNode["right"]
            long = max(leftNode["long"], rightNode["long"])
            maxValue[0] = max(
                maxValue[0],
                left+right,
                leftNode["long"] + rightNode["long"]
            )
            return {
                "left": left+1,
                "right": right+1,
                "long": long+1
            }
        myNode(root, maxValue)
        return maxValue[0]
# Runtime: 52 ms, faster than 14.30% of Python3 online submissions for Diameter of Binary Tree.
# Memory Usage: 16.7 MB, less than 20.99% of Python3 online submissions for Diameter of Binary Tree.

# 책코드
class Solution:
    longest: int = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.longest = max(self.longest, left + right)
            return max(left, right) + 1
        dfs(root)
        return self.longest
# Runtime: 48 ms, faster than 34.19% of Python3 online submissions for Diameter of Binary Tree.
# Memory Usage: 16.4 MB, less than 20.99% of Python3 online submissions for Diameter of Binary Tree.