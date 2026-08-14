class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1. Find the indices in nums2 where the nums1 elements are
        req_idx = {}
        for n in nums1:
            req_idx[n] = nums2.index(n)

        # 2. Find the next greater elements of nums2
        stack = []
        next_greater = [-1] * len(nums2)

        for idx in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[idx]:
                stack.pop()
            if stack:
                next_greater[idx] = stack[-1]
            stack.append(nums2[idx])

        # 3. For the required indices, return the next greater elements
        res = []
        for idx in req_idx.values():
            res.append(next_greater[idx])

        return res
