class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n-1:
            return False
        
        edgeMap = {i: [] for i in range(n)}
        visit = set()

        for a, b in edges:
            edgeMap[a].append(b)
            edgeMap[b].append(a)
        
        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)

            for edge in edgeMap[node]:
                if edge == prev:
                    continue
                if not dfs(edge, node):
                    return False
            return True

        if not dfs(0, 0):
            return False

        if len(visit) == n:
            return True
        return False
        