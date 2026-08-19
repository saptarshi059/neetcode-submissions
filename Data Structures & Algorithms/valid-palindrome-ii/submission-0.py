class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkpal(S):
            if S == S[::-1]:
                return True
            return False

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # Characters aren't equal. So, try to see if by deleting one, we can get a valid palindrome.
                temp1 = s[:l] + s[l+1:]
                temp2 = s[:r] + s[r+1:]
                if checkpal(temp1) or checkpal(temp2):
                    return True
                return False
        
            l += 1
            r -= 1

        return True