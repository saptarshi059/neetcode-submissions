class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            if L == R:
                break
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                R = mid - 1
            else:
                L = mid + 1

        if target > nums[L]:
            return L + 1
        else:
            return L