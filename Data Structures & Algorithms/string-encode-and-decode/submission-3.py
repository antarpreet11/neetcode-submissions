class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ''
        for s in strs:
            final += f'{len(s)}${s}'

        return final

    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            num = int(s[i:j])
            i = j + 1
            j = i + num
            strings.append(s[i:j])
            i = j
        return strings

