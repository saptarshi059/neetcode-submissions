class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1. We first try to find the point of intersection.
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # 2. Once we find the intersection, we keep slow as is & introduce another slow pointer & move both at the same speed eventually meeting at the entry point of the cycle which is the repeated element
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow