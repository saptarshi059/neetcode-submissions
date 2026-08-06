class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # This is going to hold the freq. of the top-2 elements
        counts = {}

        for n in nums:
            print(counts)
            if len(counts) < 2 or n in counts:
                counts[n] = 1 + counts.get(n, 0)
            else:
                # 0. Add the new element to counts
                counts[n] = 1
                
                # 1. Decrement counts for the seen elements
                for k in list(counts):
                    counts[k] -= 1
                    if counts[k] == 0:
                        del counts[k]

        # 2. Second pass to verify if the residual counts are actually majority.
        res = []
        des_freq = len(nums) // 3
        for k in counts:
            # This is O(n) but, not an issue here, as we only do this 2 times.
            if nums.count(k) > des_freq:
                res.append(k)

        return res