class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))
        current = 1
        longest = 1
        if len(sorted_nums) == 0:
            return 0
        
        for i in range(1,len(sorted_nums)):
            if(sorted_nums[i] - sorted_nums[i-1]) == 1:
                current +=1
            else:
                current = 1 
            longest = max(current,longest)
        return longest
        

