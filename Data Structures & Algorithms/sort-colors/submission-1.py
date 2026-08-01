class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        k = 0
        for i in range(3):
            for _ in range(counts.get(i, 0)):
                nums[k] = i
                k += 1