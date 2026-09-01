class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0 # minimum size window
        curr_sum = 0
        while r < len(nums):
            # 1. if the curr_sum is < target, keep on expanding the window, which you have to do in any case. So, no need to check. Hence, check the opposite.

            # 2. If curr_sum >= target, then try shrinking it to see if we have a valid window (curr_sum >= target)

            curr_sum += nums[r]
            while curr_sum >= target:
                if res == 0: 
                    res = r-l+1 # it has not been set yet
                else:
                    res = min(res, r-l+1)
                curr_sum -= nums[l]
                l += 1
                
            r += 1
            
        return res