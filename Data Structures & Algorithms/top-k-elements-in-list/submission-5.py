class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for _ in range(len(nums) + 1)]

        # 1. determine raw counts
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        # 2. Translate this dict to a list since there is no way to traverse a dictionary w/o sorting, which would defeat the purpose of bucket sort. 
        for n, f in counts.items():
            freq[f].append(n)

        # 3. Scan freq. in reverse and print
        final = []
        for idx in range(len(freq) - 1, 0, -1):
            for n in freq[idx]:
                final.append(n)
                if len(final) == k:
                    return final