class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            l, r = i - 1, i + 1
            currLen = 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                currLen += 2
                l -= 1
                r += 1
            if currLen > resLen:
                resLen = currLen
                res = s[l+1:r]

            l, r = i, i + 1
            currLen = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                currLen += 2
                l -= 1
                r += 1
            if currLen > resLen:
                resLen = currLen
                res = s[l+1:r]
        return res
            
