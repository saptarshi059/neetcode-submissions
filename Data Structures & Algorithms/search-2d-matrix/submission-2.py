class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            m = (top + bottom) // 2
            if target > matrix[m][-1]:
                # The target is greater than the largest element in that row
                top = m + 1
            elif target < matrix[m][0]:
                bottom = m - 1
            else:
                # top == bottom
                row = matrix[m]
                break

        if not top <= bottom:
            return False

        l, r = 0, len(row) - 1
        while l <= r:
            m = (l+r) // 2
            if row[m] == target:
                return True
            elif row[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False