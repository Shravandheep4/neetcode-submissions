import math

class MinStack:

    def __init__(self):

        self.stack = []
        self.min = math.inf
        

    def push(self, val: int) -> None:

        if val < self.min:
            self.min = val

        return self.stack.append(val)
        

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:

        if self.stack:
            return self.stack[-1]
        return None
        

    def getMin(self) -> int:
        return min(self.stack)
        
