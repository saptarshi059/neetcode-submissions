class FreqStack:

    def __init__(self):
        self.maxf = 0
        self.counts = {} # Holds the overall frequency of elements.
        self.stacks = defaultdict(list) # Holds individual stacks for frequency levels.

    def push(self, val: int) -> None:
        # 1. Update frequency of element
        self.counts[val] = 1 + self.counts.get(val, 0)

        # 2. Update max_frequency
        self.maxf = max(self.maxf, self.counts[val])

        # 3. For that frequency level, push the val
        self.stacks[self.counts[val]].append(val)

    def pop(self) -> int:
        # 1. Check if the stack associated with maxf is empty - if it is, then reduce maxf by 1 and then pop from that level
        if not self.stacks[self.maxf]:
            self.maxf -= 1
            
        top = self.stacks[self.maxf].pop()
        self.counts[top] -= 1
        return top


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()