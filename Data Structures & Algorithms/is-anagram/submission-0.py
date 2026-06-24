from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        charMap = defaultdict(int) 

        for i in range(len(s)):
            charMap[s[i]] += 1
            charMap[t[i]] -= 1
        
        for num in charMap.values():
            if num != 0:
                return False
        
        return True
        