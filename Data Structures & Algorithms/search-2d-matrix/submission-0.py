class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for l in matrix:
            for i in range(len(l)) :
                if l[i] == target:
                    return True
        return False
        