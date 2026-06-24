class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        currMap = {}
        maxLen = 0
        l = 0
        
        for r in range(len(s)):
            currMap[s[r]] = 1 + currMap.get(s[r], 0)
            while (r - l + 1) - max(currMap.values()) > k:
                currMap[s[l]] -= 1
                l += 1
            print(f"l {l}")
            print(f"r {r}")
            
            maxLen = max(maxLen, r - l + 1)
            print(f"max {maxLen}")
        return maxLen
            