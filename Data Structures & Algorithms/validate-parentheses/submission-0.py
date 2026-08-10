class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketpairs = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in bracketpairs:
                if not stack or bracketpairs[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False