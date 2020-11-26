class Codec:
    def serialize(self, root):
        answer = [None]
        q = collections.deque([root])
        while q:
            temp = []
            for _ in range(len(q)):
                # 동일 레벨의 노드 순회
                node = q.popleft()
                if node == None:
                    temp.append(None)
                    continue
                temp.append(node.val)
                q.append(node.left)
                q.append(node.right)
            for val in temp:
                if val != None:
                    answer.extend(temp)
                    break
        return answer
        

    def deserialize(self, data):
        index = 1
        if len(data) ==1 or data[index] == None:
            return None
        root = TreeNode(data[index])
        index += 1
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if index == len(data): continue # 무시
            if data[index] != None:
                node.left = TreeNode(data[index])
                q.append(node.left)
            index += 1
            if data[index] != None:
                node.right = TreeNode(data[index])
                q.append(node.right)
            index += 1
        return root