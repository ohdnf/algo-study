class Solution:
    longest = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        # 뿌린다.
        def dfs(node: TreeNode) -> tuple:
            # if node:
            #     print(f'node: {node.val}')
            # else:
            #     print(f'node: {node}')
            # (val, 연속값)
            if node == None:
                return (None, 0)
            # leafNode라면 => lvalue, lcnt = None, 0 and rvalue, rcnt = None, 0
            lval, lcnt = dfs(node.left)
            rval, rcnt = dfs(node.right)
            
            # 현재 node.val
            nval = node.val
            continous_value = 0
            returnVal = 0
            # 양쪽 값이 같을때
            if nval == lval and nval == rval:
                continous_value = lcnt + rcnt + 2
                returnVal = max(lcnt, rcnt) + 1
            # 한쪽만 같을때
            elif nval == lval:
                continous_value = lcnt + 1
                returnVal = lcnt + 1
            elif nval == rval:
                continous_value = rcnt + 1
                returnVal = rcnt + 1
            # 둘다 다를때
            # continous_value = 0, returnVal = 0
            # print(f'현재노드: {node}\n롱기스트:{self.longest}, 컨티뉴:{continous_value}')
            self.longest = max(self.longest, continous_value)
            return (nval, returnVal)
            
        dfs(root)
        return self.longest
# Runtime: 380 ms, faster than 76.71% of Python3 online submissions for Longest Univalue Path.
# Memory Usage: 18.1 MB, less than 5.52% of Python3 online submissions for Longest Univalue Path.