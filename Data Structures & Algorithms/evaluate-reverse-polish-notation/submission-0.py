class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char not in {"+", "-", "*", "/"}:
                stack.append(int(char))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if char == "+":
                    res = op2 + op1
                elif char == "-":
                    res = op2 - op1
                elif char == "*":
                    res = op2 * op1
                else:
                    res = int(op2 / op1)
                stack.append(res)
            
        return stack[-1]