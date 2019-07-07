# 74. 搜索二维矩阵

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])

        l = 0
        h = (m*n)-1

        while l<=h:
            mid = (l+h)//2
            num =  matrix[int(mid/n)][int(mid%n)]
            if target == num:
                return True
            if target < num:
                h = mid-1
            else:
                l = mid+1
        return False
