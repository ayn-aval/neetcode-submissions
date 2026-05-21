class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        n = len(nums)
        result = []
        for num in nums:
            d[num] += 1
        
        for key in d:
            if d[key] > n/3:
                result.append(key)
        return result
        