# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = ['#']
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else:
                result.append('#')
        print(result)
        return ' '.join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # string으로 되어있는 data를 split()을 통해 list로 변환한다.
        if data == "# #":
            return None 

        nodes = data.split()
        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2
    

        while queue:
            node = queue.popleft()
            if nodes[index] is not "#":
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not "#":
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root 
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))