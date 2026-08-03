class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        PP = [1] * n
        SP = [1] * n
        res = [1] * n

        for i in range(1, len(nums)):
            PP[i] = PP[i - 1] * nums[i - 1]

        for i in range(n-2, -1, -1):
            SP[i] = SP[i + 1] * nums[i + 1]

        for i in range(n):
            res[i] = PP[i] * SP[i]

        return res