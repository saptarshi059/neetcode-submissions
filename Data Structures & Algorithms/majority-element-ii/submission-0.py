class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        
        vals = []
        for n, c in counts.items():
            if c > (len(nums) // 3):
                vals.append(n)

        return vals