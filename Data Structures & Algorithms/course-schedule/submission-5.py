from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        canF = True
        preReqMap = defaultdict(list)
        visited = set()

        for course, prereq in prerequisites:
            preReqMap[course].append(prereq)

        def dfs(course):
            nonlocal canF

            if course in visited:
                canF = False
                return
            if course not in preReqMap:
                return 
            
            visited.add(course)

            for pre in preReqMap[course]:
                preReqMap[course].remove(pre)
                dfs(pre)
            
            visited.remove(course)
            return

        for course in range(numCourses):
            dfs(course)
        
        return canF
