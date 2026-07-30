class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Iterate through array
        # 2. Create hash values and add to map if not present
        # 3. If hash present, add string to value list

        anagrams = {}
        for s in strs:
            hash_array = [0] * 26
            for char in s:
                idx = ord(char) - ord('a')
                hash_array[idx] += 1
            if tuple(hash_array) in anagrams:
                anagrams[tuple(hash_array)].append(s)
            else:
                anagrams[tuple(hash_array)] = [s]
        return list(anagrams.values())