class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c : set() for w in words for c in w}

        for i in range(len(words) - 1): 
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        result = []
        visit = set()
        visiting = set()

        def dfs(ch):
            if ch in visiting:
                return False
            if ch in visit:
                return True
            
            visiting.add(ch)

            for nei in adj[ch]:
                if not dfs(nei):
                    return False
            
            visiting.remove(ch)
            visit.add(ch)
            result.append(ch)
            return True

        for ch in adj:
            if not dfs(ch):
                return ""

        result.reverse()
        return "".join(result)

