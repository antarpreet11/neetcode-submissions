class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        canF = True

        for p in prerequisites:
            if preMap.get(p[0]):
                preMap[p[0]] = preMap[p[0]] + [p[1]]
            else:
                preMap[p[0]] = [p[1]]
        
        visited = set()

        def dfs(c):
            nonlocal canF
            
            if c in visited:
                canF = False
                return

            if c not in preMap:
                return

            visited.add(c)

            for p in preMap[c]:
                preMap[c].remove(p)
                dfs(p)

            visited.remove(c)
            return
            

        for course in preMap.keys():
            dfs(course)
        
        return canF