class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))
        res = 1
        for num in sorted_nums:
            if num == res:
                res +=1
        return res
       
