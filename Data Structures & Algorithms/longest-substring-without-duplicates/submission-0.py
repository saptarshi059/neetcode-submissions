class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_size = 0
        l,r = 0,0
        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            max_size = max(len(window), max_size)
            r += 1
        
        return max_size