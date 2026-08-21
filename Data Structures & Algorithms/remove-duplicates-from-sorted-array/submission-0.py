class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        while j < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            
            if j < len(nums) and (i+1) < len(nums):
                nums[i+1] = nums[j]
                i += 1
                j += 1
        
        return i + 1

