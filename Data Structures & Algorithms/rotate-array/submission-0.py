class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. Find effective rotations - This is because, say the length of the array is 3 and k = 3. That means, after 3 rotations, you'd be at square one. If k = 4, then you'd actually have to do just 1 rotation.
        n = len(nums)
        k = k % n

        def rot(L, R, nums):
            while L < R:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
                R -= 1
        
        # 2. Rotate the entire array
        rot(0, n-1, nums)
        # 3. Rotate first k-elements
        rot(0, k-1, nums)
        # 4. Rotate k+1 to end elements
        rot(k, n-1, nums)