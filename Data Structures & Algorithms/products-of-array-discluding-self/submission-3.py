class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Optimal version (no extra arrays)
        # 1. Create prefix products (all vals except current) and store in res
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # 2. Determine suffix and directly add to the prefix
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res