class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        number_stack = []
        idx = 0
        while idx < len(s):
            # 1. Check for numbers
            num = ""
            while s[idx].isdigit():
                num += s[idx]
                idx += 1
                continue
            if num != "":
                number_stack.append(int(num))

            substring = ""
            if s[idx] == "]":
                temp = []
                while string_stack and string_stack[-1] != "[":
                    temp.append(string_stack.pop())
                string_stack.pop() # For the "["
                substring = "".join(temp[-1::-1])

            if substring:
                string_stack.append(substring * number_stack.pop())
            else:
                string_stack.append(s[idx])

            idx += 1

        final_string = "".join(string_stack)
        return final_string