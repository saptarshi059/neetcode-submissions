class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Practicing Boyer-Moore - forgot about it lol
        res, count = nums[0], 1
        
        # Starting from 1 because I've already seen the 0th index
        for i in range(1, len(nums)):
            if res == nums[i]:
                count += 1
            else:
                count -= 1

            if count == 0:
                res = nums[i]
                count = 1

        return res