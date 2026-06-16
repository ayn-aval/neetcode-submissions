class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        new_array = []
        for i in range((len(nums)-k)+1):
            sub_array = nums[i:i+k]
            res = max(sub_array)
            new_array.append(res)
        return new_array