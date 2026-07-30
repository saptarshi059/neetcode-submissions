class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        floor = n // 2
        counts = {}
        for v in nums:
            counts[v] = 1 + counts.get(v, 0)
        return list(filter(lambda x: x[1] > floor, counts.items()))[0][0]