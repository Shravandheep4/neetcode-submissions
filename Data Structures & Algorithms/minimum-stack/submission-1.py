class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.length = 0
        self.stack = []
        

    def push(self, val: int) -> None:

        self.stack.append((val, self.min))

        self.min = min(val, self.min)
        self.length += 1

        

    def pop(self) -> None:
        _, previous_minimum = self.stack.pop()
        self.min = previous_minimum
        self.length -= 1
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min
        
