class Solution:
    def rob(self, nums: List[int]) -> int:
        resMap = {}
        
        def dp(index):
            if index >= len(nums):
                return 0
            
            if index in resMap:
                return resMap[index]

            res = max(nums[index] + dp(index + 2), dp(index + 1))
            resMap[index] = res
            return res

        return dp(0)