class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n*(n+1)/2
        array_sum = sum(nums)
        missing_num = total_sum - array_sum
        return int(missing_num)