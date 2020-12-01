# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        queue = collections.deque()
        queue.append(root)

        ser = 'X'

        while queue:
            node = queue.popleft()
            if node:
                ser += ' ' + str(node.val)

                queue.append(node.left)
                queue.append(node.right)

            else:
                ser += ' X'

        return ser

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        nodes = data.split()

        if nodes[1] == 'X':
            return None

        root = TreeNode(int(nodes[1]))

        queue = collections.deque()
        queue.append(root)
        index = 2

        while queue:
            node = queue.popleft()
            if nodes[index] != 'X':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] != 'X':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

"""
Runtime: 112 ms, faster than 78.94% of Python3 online submissions for Serialize and Deserialize Binary Tree.
Memory Usage: 18.8 MB, less than 35.68% of Python3 online submissions for Serialize and Deserialize Binary Tree.
"""


# Discuss 2위 풀이

class Codec:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()
