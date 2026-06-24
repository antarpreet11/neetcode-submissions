class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def checkLongest(i, odd):
            nonlocal res
            nonlocal resLen
            l = i
            r = i if odd else i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            return

        for i in range(len(s)):
            checkLongest(i, True)
            checkLongest(i, False)
        
        return res