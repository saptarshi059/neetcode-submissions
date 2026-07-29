class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def char_counter(string):
            counts = {}
            for char in string:
                if char in counts:
                    counts[char] += 1
                else:
                    counts[char] = 1
            return counts
        
        if char_counter(s) == char_counter(t):
            return True
        else:
            return False
