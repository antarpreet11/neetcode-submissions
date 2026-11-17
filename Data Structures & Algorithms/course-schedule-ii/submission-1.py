from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        res = []
        visiting = set()

        for prereq in prerequisites:
            preMap[prereq[0]].append(prereq[1])
        
        def dfs(num: int) -> bool:
            nonlocal visiting

            if num in visiting:
                return False

            if num in res:
                return True
            
            visiting.add(num)
            
            for pre in preMap[num]:
                if not dfs(pre):
                    return False
            
            visiting.remove(num)
            res.append(num)

            return True


        for num in range(numCourses):
            if not dfs(num):
                return []
        
        return res
        
        