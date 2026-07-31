class Solution:
    def hammingWeight(self, n: int) -> int:
        n_bin = bin(n)[2:]
        count = 0
        for chr in n_bin:
            if chr == '1':
                count += 1
        return count