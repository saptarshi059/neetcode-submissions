class Solution:
    def isPalindrome(self, s: str) -> bool:
        def checkvalid(c):
            cond1 = ord("A") <= ord(c) <= ord("Z")
            cond2 = ord("a") <= ord(c) <= ord("z")
            cond3 = ord("0") <= ord(c) <= ord("9")
            if cond1 or cond2 or cond3:
                return True
            return False
        
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not checkvalid(s[l]):
                l += 1
            while r > l and not checkvalid(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True
