class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        i = 0
        res = []
        while i < len(nums):
            target = 0 - nums[i]
            subarray = nums[i + 1:]
            L = i + 1
            R = len(nums) - 1
            while L < R:
                s = nums[L] + nums[R]
                if s == target:
                    res.append((nums[i], nums[L], nums[R]))
                if s > target:
                    R -= 1
                else:
                    L += 1
            i += 1
        
        return list(set(res))