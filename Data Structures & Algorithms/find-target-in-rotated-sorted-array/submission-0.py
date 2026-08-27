class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. find pivot
        def binary_search(array):
            l, r = 0, len(array) - 1
            while l < r:
                m = (l + r) // 2
                if array[m] > array[r]:
                    l += 1
                else:
                    r = m
            return l

        def bs(array, t):
            l, r = 0, len(array) - 1
            while l <= r:
                m = (l + r) // 2
                if array[m] == t:
                    return m
                if t > array[m]:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        pivot_idx = binary_search(nums)

        # 2. Based on pivot limits, run binary search
        if pivot_idx == 0:
            return bs(nums, target)
        elif nums[0] <= target <= nums[pivot_idx-1]:
            # search left
            return bs(nums[0:pivot_idx], target)
        else:
            idx = bs(nums[pivot_idx:], target)
            if idx == -1:
                return -1
            else:
                return pivot_idx + idx