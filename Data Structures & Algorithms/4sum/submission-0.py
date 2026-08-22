class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                L, R = j+1, n - 1
                while L < R:
                    s = nums[i] + nums[j] + nums[L] + nums[R]
                    if s == target:
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        L += 1
                        R -= 1
                        while L < R and nums[L] == nums[L-1]:
                            L += 1
                        while L < R and nums[R] == nums[R+1]:
                            R -= 1
                    elif s < target:
                        L += 1
                    else:
                        R -= 1
        return res