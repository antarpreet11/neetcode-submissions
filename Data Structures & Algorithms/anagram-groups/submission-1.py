from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupByChar = defaultdict(list)

        for s in strs:
            charList = [0 for _ in range(26)]
            for c in s:
                charList[ord(c) - ord('a')] += 1
            groupByChar[tuple(charList)].append(s)
        
        return list(groupByChar.values())
