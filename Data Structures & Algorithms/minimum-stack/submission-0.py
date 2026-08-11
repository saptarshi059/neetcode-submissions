class MinStack:

    def __init__(self):
        self.stack = []
        self.minq = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minq or val <= self.minq[-1]:
            self.minq.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minq[-1]:
            self.minq.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minq[-1]