class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList = [[] for i in range(len(nums) + 1)]
        freqMap = {}
        res = []

        for n in nums:
            freqMap[n] = 1 + freqMap.get(n, 0)
        
        for n, freq in freqMap.items():
            freqList[freq].append(n)

        for i in range(len(freqList) - 1, -1, -1):
            for n in freqList[i]:
                res.append(n)
                if len(res) == k:
                    return res
        