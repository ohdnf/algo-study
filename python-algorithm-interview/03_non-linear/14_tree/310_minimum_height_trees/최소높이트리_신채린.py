# 최소 높이를 구성하려면 가장 가운데에 있는 값이 루트여야 한다.
# 이 말은 리프 노드를 하나씩 제거해 나가면서 남아있는 값을 찾으면, 
# 이 값이 가장 가운데에 있는 값이 될 것이고, 이 값을 루트로 했을 때 
# 최소 높이를 구성할 수 있다는 뜻이다. 

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]
        
        # 양방향 그래프 구성 
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i) 
        
        # 첫번째 리프 노드 추가 
        leaves = []
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)
                
        # 루트 노드만 남을때까지 반복 제거 
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop() 
                graph[neighbor].remove(leaf)
                
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves