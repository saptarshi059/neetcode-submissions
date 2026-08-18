from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.sos = defaultdict(list) # stack-of-stack (key = freq. level | val = stack at that freq. level).
        self.freq = defaultdict(list) # frequencies of all elements.
        self.max_cnt = 0 # highest frequency among all elements.

    def push(self, val: int) -> None:
        self.freq[val] = 1 + self.freq.get(val, 0)
        
        # 1. If the frequency of the most recently added element is greater than previous max freq, update it.
        if self.freq[val] > self.max_cnt:
            self.max_cnt = self.freq[val]

        # 2. For this frequency level append to the stack
        self.sos[self.freq[val]].append(val)

    def pop(self) -> int:
        # 1. Find the stack associated with the max freq.
        max_freq_stack = self.sos[self.max_cnt]

        # 2. If the max_freq_stack is NOT empty, then pop the top from this stack and decrement count of the top element
        if max_freq_stack:
            top = max_freq_stack.pop()
            self.freq[top] -= 1
            return top
        else:
            # max_freq_stack is empty, so, decrease count first and then return from the next one.
            self.max_cnt -= 1
            next_best_stack = self.sos[self.max_cnt]
            top = next_best_stack.pop()
            self.freq[top] -= 1
            return top



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()