from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSum = defaultdict(int)
        prefixSum[0] = 1

        currSum = 0

        for n in nums:
            currSum += n
            diff = currSum - k

            if diff in prefixSum:
                res += prefixSum[diff]
            prefixSum[currSum] += 1
        return res
