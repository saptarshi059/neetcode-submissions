class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sos = set()
        nums = set(nums)
        for n in nums:
            if (n-1) not in nums:
                # This means the current number CAN start a sequence
                sos.add(n)

        max_len = 0
        for s in sos:
            curr_seq_len = 1
            start = s
            while (start+1) in nums:
                curr_seq_len += 1
                start += 1
            max_len = max(max_len, curr_seq_len)

        return max_len