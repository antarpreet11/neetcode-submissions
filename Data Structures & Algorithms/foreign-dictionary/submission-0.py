class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c : set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            length = min(len(w1), len(w2))

            if w1[:length] == w2[:length] and len(w1) > len(w2):
                return ""

            for c in range(length):
                if w1[c] != w2[c]:
                    adj[w1[c]].add(w2[c])
                    break
        
        visit = {} # False=visited, True=current path
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True

            visit[c] = False
            res.append(c)

        for char in adj: 
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)

