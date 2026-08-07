class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stack = []
        for n in operations:
            if n not in {"+", "D", "C"}:
                score_stack.append(int(n))
            elif n == "+":
                sum_element = score_stack[-1] + score_stack[-2]
                score_stack.append(sum_element)
            elif n == "D":
                prod = 2 * score_stack[-1]
                score_stack.append(prod)
            else:
                score_stack.pop()
        return sum(score_stack)