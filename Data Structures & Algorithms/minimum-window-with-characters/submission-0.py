class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) :
            return ""
        
        res = ""
        count = {}
        l = 0
        have = 0

        for c in t: 
            count[c] = 1 + count.get(c, 0)
        need = len(count)

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] -= 1
                if count[s[r]] == 0:
                    have += 1

            while need == have:
                currLen = r - l + 1
                if len(res) > currLen or not res:
                    res = s[l:r+1]
                if s[l] in count:
                    count[s[l]] += 1
                    if count[s[l]] == 1:
                        have -= 1
                l += 1
        return res