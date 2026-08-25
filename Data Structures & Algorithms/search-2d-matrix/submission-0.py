class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for idx, row in enumerate(matrix):
            s, e = row[0], row[-1]
            if s <= target <= e:
                # Found our target row
                break

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