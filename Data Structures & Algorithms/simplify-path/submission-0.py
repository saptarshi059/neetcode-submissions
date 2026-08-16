class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        idx = 0
        while idx < len(path):
            # 1. Collect current directory
            curr = ""
            while idx < len(path) and path[idx] != "/":
                curr += path[idx]
                idx += 1

            # 2. Check where we are
            if curr == ".." and stack:
                # Going back to the parent directory
                stack.pop()
            elif curr not in {".", "..", ""}:
                stack.append(curr)

            idx += 1

        if not stack:
            return "/"

        canonical_path = "/" + "/".join(stack)
        return canonical_path