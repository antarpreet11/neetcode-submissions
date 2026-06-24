class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currSet = set()
        maxLen = 0

        l = 0

        for r in range(len(s)):
            while s[r] in currSet:
                currSet.remove(s[l])
                l += 1    

            currSet.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        return maxLen

        
