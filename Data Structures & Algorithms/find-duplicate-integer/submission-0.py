class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}

        for n in nums:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1

        for num, count in seen.items():
            if count > 1:
                return num

    