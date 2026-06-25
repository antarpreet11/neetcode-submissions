class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        results = [intervals[0]]

        for i in range(1, len(intervals)):
            first = results[-1]
            second = intervals[i]

            if first[1] >= second[0]:
                results[-1][1] = max(first[1], second[1])
            else:
                results.append(second)

        return results
    
        