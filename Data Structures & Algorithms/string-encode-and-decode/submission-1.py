class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ''
        for str in strs:
            length = len(str)
            final += f'{length}${str}'

        return final

    def decode(self, s: str) -> List[str]:
        strings = []
        
        while s:
            i = s.index("$")
            num = int(s[:i])
            strings.append(s[i+1:i+num+1])
            s = s[i+num+1:] 
        return strings