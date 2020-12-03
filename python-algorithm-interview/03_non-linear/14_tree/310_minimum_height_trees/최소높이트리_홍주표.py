class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # height for each node when it is root
        heights = [-1] * n

        # adjacent matrix for edges
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        roots = []
        self.min_height = float('inf')

        for root in range(n):
            if heights[root] != -1:
                max_height = heights[root]
            else:
                visited = [False] * n
                visited[root] = True

                max_height = 0
                queue = collections.deque()
                queue.append((root, 1))

                while queue:
                    node, height = queue.popleft()
                    visited[node] = True

                    if max_height < height:
                        max_height = height

                    for next_node in adj[node]:
                        if not visited[next_node]:
                            queue.append((next_node, height + 1))

                heights[root] = max_height

            if self.min_height > max_height:
                self.min_height = max_height
                roots.clear()
                roots.append(root)
            elif self.min_height == max_height:
                roots.append(root)

        return roots

"""
5000개 노드일 때 Time Limit Exceeded
"""


# Solution 보고 구현한 topological sorting
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        connection = [0] * n

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            connection[u] += 1
            adj[v].append(u)
            connection[v] += 1

        queue = collections.deque()
        roots = set(range(n))

        while len(roots) > 2:
            for node, count in enumerate(connection):
                if count == 1:
                    queue.append(node)

            while queue:
                node = queue.popleft()
                connection[node] -= 1
                roots.remove(node)
                for other in adj[node]:
                    connection[other] -= 1

        return roots

"""
Runtime: 940 ms, faster than 6.54% of Python3 online submissions for Minimum Height Trees.
Memory Usage: 18.9 MB, less than 31.82% of Python3 online submissions for Minimum Height Trees.
"""


# Solution(Python)
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # base cases
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                # remove the only edge left
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        return leaves

"""
Runtime: 236 ms, faster than 54.69% of Python3 online submissions for Minimum Height Trees.
Memory Usage: 18.9 MB, less than 31.82% of Python3 online submissions for Minimum Height Trees.
"""
