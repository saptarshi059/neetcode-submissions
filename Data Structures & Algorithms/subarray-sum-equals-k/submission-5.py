class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps = {0:1}
        res = 0
        S = 0
        for n in nums:
            S += n
            comp = S - k
            res = res + ps.get(comp, 0)
            # At each index, the sum becomes the prefix sum for the next index. That's why we have to add it to the ps table.
            ps[S] = 1 + ps.get(S, 0)
            
    
        return res