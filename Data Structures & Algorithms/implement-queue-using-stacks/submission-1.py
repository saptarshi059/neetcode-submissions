class MyQueue:

    def __init__(self):
        # s1 is for pushing elements into stack
        # s2 is for popping elements
        self.s1, self.s2 = [], []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        # 1. Transfer all elements in reverse order (because stack allows only top element access) from s1 to s2, if s2 is empty - the moment it becomes empty, you pop
        if self.s2 == []:
            for _ in range(len(self.s1)):
                self.s2.append(self.s1.pop())

        # 2. Return element from s2
        return self.s2.pop()

    def peek(self) -> int:
        if self.s2 == []:
            for _ in range(len(self.s1)):
                self.s2.append(self.s1.pop())

        # 2. Return element from s2
        return self.s2[-1]

    def empty(self) -> bool:
        if self.s1 == [] and self.s2 == []:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()