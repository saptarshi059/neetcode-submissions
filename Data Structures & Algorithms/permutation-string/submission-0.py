class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # 1. Compute frequency map of s1
        s1_freq = {}
        for char in s1:
            s1_freq[char] = 1 + s1_freq.get(char, 0)

        window_freq = {}
        for i in range(len(s1)):
            window_freq[s2[i]] = 1 + window_freq.get(s2[i], 0)

        l, r = 0, len(s1) - 1
        while r < len(s2):
            # Check if window freq is same as s1_freq
            print(window_freq)
            if window_freq == s1_freq:
                return True

            # Decrease counts of l since it leaves the window completely
            window_freq[s2[l]] -= 1
            
            # Check if those counts are 0
            if s2[l] in window_freq and window_freq[s2[l]] == 0:
                window_freq.pop(s2[l])

            # Move window pointers
            l += 1
            r += 1

            # Add r element
            if r < len(s2):
                window_freq[s2[r]] = 1 + window_freq.get(s2[r], 0)

        return False