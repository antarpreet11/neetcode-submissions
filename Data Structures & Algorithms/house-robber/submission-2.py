class Solution:
    def rob(self, nums: List[int]) -> int:
        prevprev, prev = 0, 0
        
        for num in nums:
            temp = max(prev, prevprev + num)
            prevprev = prev
            prev = temp
        return prev