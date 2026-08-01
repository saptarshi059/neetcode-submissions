class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for word in strs:
            enc += f"{len(word)}#{word}"
        return enc

    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0
        while i < len(s):
            # 1. Collect the number characters
            length_str = ""
            while s[i] != "#":
                length_str += s[i]
                i += 1
            i += 1 # To account for the special character
            word_length = int(length_str)

            # 2. Then process the word
            word = ""
            while i < len(s) and word_length > 0:
                word += s[i]
                i += 1
                word_length -= 1
            dec.append(word)
        return dec
