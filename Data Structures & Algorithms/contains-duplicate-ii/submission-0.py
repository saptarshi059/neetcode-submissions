class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        i, j = 0, 0
        while j < len(nums):
            # 1. Check for valid window 
            if abs(j - i) <= k:
                if nums[j] in window:
                    return True
                window.add(nums[j])
                j += 1
            else:
                # Window is invalid - thus, pop the leftmost element to make the window valid again
                window.remove(nums[i])
                i += 1

        return False