class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        timesInt = []
        minTime = 24 * 60

        for i in range(len(timePoints)):
            time = timePoints[i]
            h, m = time.split(":")
            timesInt.append([int(h), int(m)])

        for i in range(1, len(timesInt)):
            total = (timesInt[i][0] - timesInt[i - 1][0]) * 60
            total += (timesInt[i][1] - timesInt[i - 1][1])
            minTime = min(minTime, total)
        
        # First and Last
        oppTime = (timesInt[0][0] + 24 - timesInt[-1][0]) * 60
        oppTime += (timesInt[0][1] - timesInt[-1][1])
        minTime = min(minTime, oppTime)

        return minTime
