class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        max_length = 0
        for ch in s:
            while ch in window:
                window.pop(0)
            window.append(ch)
            max_length = max(max_length,len(window))
        return max_length