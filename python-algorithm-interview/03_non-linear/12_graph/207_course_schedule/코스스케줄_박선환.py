class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = dict()
        for a, b in prerequisites:
            try:
                graph[a].append(b)
            except:
                graph[a] = [b]

        traced = []
        visited = []

        def dfs(node):
            if node in traced:
                return False
            if node in visited:
                return True
            
            traced.append(node)
            try:
                for n_node in graph[node]:
                    if not dfs(n_node):
                        return False
            except:
                pass
            traced.remove(node)
            visited.append(node)
            return True
        
        for node in graph:
            if not dfs(node):
                return False
            
        return True