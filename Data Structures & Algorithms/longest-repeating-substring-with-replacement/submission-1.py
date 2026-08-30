class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {} # Count of characters in the window
        res = 0 # length of the longest substring
        l,r = 0,0
        maxf = 0
        while r < len(s):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            maxf = max(maxf, counts[s[r]])

            # Check if the window is valid, if not, shrink
            while (r-l+1) - maxf > k:
                counts[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
            r += 1
        
        return res