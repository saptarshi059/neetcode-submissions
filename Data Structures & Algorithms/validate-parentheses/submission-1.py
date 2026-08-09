class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]
        for char in s[1:]:
            if char in {"(", "{", "["}:
                stack.append(char)
            elif char == ")":
                if stack:
                    top = stack.pop()
                    if top != "(":
                        return False
                else:
                    # For an empty stack
                    return False
            elif char == "}":
                if stack:
                    top = stack.pop()
                    if top != "{":
                        return False
                else:
                    # For an empty stack
                    return False
            elif char == "]":
                if stack:
                    top = stack.pop()
                    if top != "[":
                        return False
                else:
                    # For an empty stack
                    return False

        if stack != []:
            return False
        else:
            return True