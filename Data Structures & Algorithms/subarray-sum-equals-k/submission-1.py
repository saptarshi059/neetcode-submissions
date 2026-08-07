class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0:1}
        S, res = 0, 0

        for n in nums:
            S += n
            comp = S - k
            res += prefix_sums.get(comp, 0)
            prefix_sums[S] = 1 + prefix_sums.get(S, 0)
        
        return res
