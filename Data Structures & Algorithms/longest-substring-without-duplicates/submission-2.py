class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currSet = set()
        maxLen = 0

        l = 0

        for r in range(len(s)):

            if s[r] not in currSet:
                currSet.add(s[r])
            else:
                while s[r] in currSet:
                    currSet.remove(s[l])
                    l += 1
                currSet.add(s[r])
            maxLen = max(r - l + 1, maxLen)
        return maxLen

        
