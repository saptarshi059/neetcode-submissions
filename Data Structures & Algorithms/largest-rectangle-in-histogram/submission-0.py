class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (H, starting index from where we can extend this height)
        max_area = 0
        n = len(heights)
        for idx, h in enumerate(heights):
            if not stack:
                # Empty stack
                stack.append((h, idx))
            else:
                prev_idx = idx
                while stack and stack[-1][0] > h:
                    top = stack.pop()
                    width = idx - top[1]
                    height = top[0] # The bar we could not extend
                    area = width * height
                    max_area = max(max_area, area)
                    prev_idx = top[1]
                
                stack.append((h, prev_idx))

        # Checking for remaining elements
        while stack:
            top = stack.pop()
            w = n - top[-1]
            h = top[0]
            a = w * h
            max_area = max(max_area, a)

        return max_area
