class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j=0
        for chr in s:
            if j < len(t) and chr == t[j]:
                j += 1
        return len(t) - j
