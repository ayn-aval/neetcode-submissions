class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()

        l = 0
        r = len(num) -1 
        n = len(num)
        res = 0

        k = (l+r) // 2
        if n % 2 == 0:
            res = (num[k] + num[k+1])/2
        else :
            res = num[k] 
        return res 
            

        