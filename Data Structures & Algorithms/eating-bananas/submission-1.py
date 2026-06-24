import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxNum = max(piles)
        l, r = 1, maxNum
        res = r

        while l <= r:
            k = l + ((r - l) // 2)

            hours = 0
            for p in piles:
                hours += p // k 
                if (p % k) > 0:
                    hours += 1
            
            if hours <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
                    
        return res