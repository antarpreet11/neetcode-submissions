class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        reqs = {}
        for ch in t:
            reqs[ch] = 1 + reqs.get(ch, 0)

        need = len(reqs)
        res = ""

        l = 0
        for r in range(len(s)):
            if s[r] in reqs:
                reqs[s[r]] -= 1
                if reqs[s[r]] == 0:
                    need -= 1
            
            while need == 0:
                if not res or len(res) > (r - l + 1):
                    res = s[l:r+1]
                
                if s[l] in reqs:
                    reqs[s[l]] += 1
                    if reqs[s[l]] == 1:
                        need += 1
                l += 1
        return res
