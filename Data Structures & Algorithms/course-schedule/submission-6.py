from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqMap = defaultdict(list)
        visiting = set()

        for course, prereq in prerequisites:
            preReqMap[course].append(prereq)

        def dfs(course):
            if course in visiting:
                return False
            if preReqMap[course] == []:
                return True 

            visiting.add(course)
            for pre in preReqMap[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            preReqMap[course] = []
            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
