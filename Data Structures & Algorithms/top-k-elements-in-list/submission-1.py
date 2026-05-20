class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        return sorted(d, key=d.get,reverse=True)[:k]