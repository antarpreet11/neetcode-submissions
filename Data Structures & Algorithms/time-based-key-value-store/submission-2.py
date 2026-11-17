from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.data = defaultdict(TimeData)

    def set(self, key: str, value: str, timestamp: int) -> None:
        dataPoint = self.data[key]
        dataPoint.times.append(timestamp)
        dataPoint.values[timestamp] = value
        return

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        if timestamp in self.data[key].values:
            return self.data[key].values[timestamp]
        
        bestTs = self.binarySearch(self.data[key].times, timestamp)
        if bestTs < 0:
            return ""
        return self.data[key].values[bestTs]
        
    def binarySearch(self, times: list, ts: int) -> int:
        result = -1  
        start, end = 0, len(times)-1

        while start <= end:
            mid = (start + end) // 2
            
            if times[mid] <= ts:
                result = times[mid]
                start = mid + 1
            else:
                end = mid - 1
        return result

class TimeData:
    def __init__(self):
        self.times = []
        self.values = {}