class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count= self.Bin(i)
            res.append(count)
        return res

    def Bin(self, k:int) -> int:
        k_bin = bin(k)[2:]
        count = 0
        for chr in k_bin :
            if chr == '1':
                count += 1
        return count 


