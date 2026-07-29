class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for element in nums:
            if element in seen:
                return True
            else:
                seen.add(element)
        return False