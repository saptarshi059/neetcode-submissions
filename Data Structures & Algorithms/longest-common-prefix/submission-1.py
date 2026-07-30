class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        shortest_string = min(strs, key=len)
        for idx, char in enumerate(shortest_string):
            for s in strs:
                if s[idx] != char:
                    return common
            common += char
        return common