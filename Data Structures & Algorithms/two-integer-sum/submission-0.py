class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mmap = {}
        for i, n in enumerate(nums): 
            diff = target - n
            if diff in mmap:
                return [mmap[diff], i] 
            mmap[n] = i