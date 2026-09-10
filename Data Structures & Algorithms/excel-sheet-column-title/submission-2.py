class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber != 0:
            columnNumber -= 1 # To account for 1-indexing
            res.append(chr(ord('A') + columnNumber % 26))
            columnNumber //= 26
        
        return ''.join(res[-1::-1])