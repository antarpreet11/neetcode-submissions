class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def check(i, odd):
            nonlocal count
            l = i
            r = i if odd else i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return

        for i in range(len(s)):
            check(i, True)
            check(i, False)
        
        return count
