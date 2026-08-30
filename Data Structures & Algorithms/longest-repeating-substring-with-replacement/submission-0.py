class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {} # Count of characters in the window
        res = 0 # length of the longest substring
        l,r = 0,0
        maxf = 0
        while r < len(s):
            # 1. Check if the current window is valid: window length - count of max character <= k because once you remove the max freq. character in that window, you are left with all other characters that need replacement. If you can do that within k moves, then you are fine.
            window_len = (r - l) + 1
            counts[s[r]] = 1 + counts.get(s[r], 0)
            maxf = max(maxf, counts[s[r]])
            while window_len - maxf > k:
                # This means that the window is invalid so start shrinking it
                counts[s[l]] -= 1
                maxf = max(counts.values())
                l += 1
                window_len -= 1

            res = max(res, window_len)
            r += 1
        return res