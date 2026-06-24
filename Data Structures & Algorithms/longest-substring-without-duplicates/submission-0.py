class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currSet = set()
        maxLen = 0

        l, r = 0, 0

        while r < len(s):
            while s[r] in currSet:
                currSet.remove(s[l])
                l += 1    

            currSet.add(s[r])
            r += 1
            maxLen = max(maxLen, r - l)
        return maxLen

        
