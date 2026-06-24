class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for n in nums:
            numSet.add(n)

        maxLength = 0
        
        for n in nums:
            temp = 1
            if n-1 not in numSet:
                num = n+1
                while num in numSet:
                    temp += 1
                    num += 1
            maxLength = max(maxLength, temp)
        return maxLength
                