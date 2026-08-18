class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq[val] = 1 + self.freq.get(val, 0)

    def pop(self) -> int:
        max_freq = max(self.freq.items(), key=lambda x: x[1])[1]
        max_freq_els = []
        for k, v in self.freq.items():
            if v == max_freq:
                max_freq_els.append(k)

        temp = []
        while self.stack and self.stack[-1] not in max_freq_els:
            top = self.stack.pop()
            temp.append(top)
            self.freq[top] -= 1

        if self.stack:
            top = self.stack.pop()
            self.freq[top] -= 1
            most_freq_el = top
        else:
            most_freq_el = None

        for el in temp:
            self.stack.append(el)
            self.freq[el] += 1

        return most_freq_el



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()