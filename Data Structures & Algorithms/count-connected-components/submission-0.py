class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = set()
        res = 0

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)
            
            for edge in adj[node]:
                dfs(edge)


        for v in range(n):
            if v not in visit:
                res += 1
                dfs(v)

        return res