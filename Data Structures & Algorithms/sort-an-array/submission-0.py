class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(L, R, nums):
            i, j, k = 0, 0, 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i += 1
                    k += 1
                else:
                    nums[k] = R[j]
                    j += 1
                    k += 1
            
            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1
            
            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1

        num_elements = len(nums)
        if num_elements > 1:
            mp = num_elements // 2
            L = self.sortArray(nums[:mp])
            R = self.sortArray(nums[mp:])
            merge(L, R, nums)
        return nums