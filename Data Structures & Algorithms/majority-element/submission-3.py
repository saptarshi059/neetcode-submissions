class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # This solution is just to learn NC's way of doing it. Much cleaner.

        res, maxC = 0, 0
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
            if counts[n] > maxC:
                res = n
                maxC = counts[n]
        return res