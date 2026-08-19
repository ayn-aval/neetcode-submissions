class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1:
            return len(s)
        
        hashset = set()
        L = 0
        R = 0
        res = 0

        while R < len(s):

            if s[R] not in hashset:
                res = max(res, R - L + 1)
                hashset.add(s[R])
                R = R + 1
            else :  
                while L <= R < len(s) and s[R] in hashset:
                    hashset.remove(s[L])
                    L = L + 1
        
        return res
        