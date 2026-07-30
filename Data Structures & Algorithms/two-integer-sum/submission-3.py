class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_dict = {}
        for idx, n in enumerate(nums):
            comp = target - n
            if comp not in complement_dict:
                complement_dict[n] = idx
            else:
                return [complement_dict[comp], idx]