class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res  = []
        
        for i in range(n):
            forward = 1
            backward = 1

            for j in range(i):
                backward *= nums[j]
            for j in range(i+1,n):
                forward *= nums[j]
            Total = forward * backward 
            res.append(Total)
        return res

        