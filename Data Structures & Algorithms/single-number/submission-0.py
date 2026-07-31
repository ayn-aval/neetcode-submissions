class Solution:
    
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for n in nums:
            d[n] += 1

        for num, count in d.items():
            if count == 1:
                return num