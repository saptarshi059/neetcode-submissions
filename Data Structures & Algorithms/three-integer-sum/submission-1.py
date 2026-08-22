class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        i = 0
        res = []
        while i < len(nums):
            # Have to check if we have already explored the current element which might be a duplicate
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            L = i + 1
            R = len(nums) - 1
            while L < R:
                s = nums[i] + nums[L] + nums[R]
                if s == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
                elif s > 0:
                    R -= 1
                else:
                    L += 1
            i += 1
        
        return res