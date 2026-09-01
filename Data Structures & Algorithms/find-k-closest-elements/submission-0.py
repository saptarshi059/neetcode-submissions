class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r = 0, len(arr) - 1
        while r - l >= k:
            # Check which element is farther away from x and move its pointer inward
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1
        return arr[l:r+1]