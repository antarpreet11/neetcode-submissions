class Solution:
    def climbStairs(self, n: int) -> int:
        curr, next = 1, 1

        for i in range(n - 2, -1, -1):
            new = curr + next
            next = curr
            curr = new
        
        return curr