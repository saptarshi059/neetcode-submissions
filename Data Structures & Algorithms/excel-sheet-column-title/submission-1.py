class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = {}
        s = "abcdefghijklmnopqrstuvwxyz"
        for idx, char in enumerate(s):
            alphabet[idx+1] = char.upper()
        
        res = []
        while columnNumber != 0:
            rem = columnNumber % 26
            if rem == 0:
                char = "Z"
            else:
                char = alphabet[rem]
            res.append(char)
            if rem == 0:
                break
            columnNumber = columnNumber // 26

        return ''.join(res[-1::-1])