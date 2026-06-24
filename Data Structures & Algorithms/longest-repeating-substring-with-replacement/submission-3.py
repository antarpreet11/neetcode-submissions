class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = [0] * 26
        l = 0
        maxLen = 0
        maxF = 0

        for r in range(len(s)):
            index = ord(s[r]) - ord('A')
            charCount[index] += 1
            maxF = max(maxF, charCount[index])
            
            while (r - l + 1) - maxF > k:
                index = ord(s[l]) - ord('A')
                charCount[index] -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)
        return maxLen

         