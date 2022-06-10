    def __init__(self):
        self.MinStack=[]
    def push(self, val: int) -> None:
        self.MinStack.append(val)
    def pop(self) -> None:
        self.MinStack.pop()
    def top(self) -> int:
        if MinStack:
            return self.MinStack[-1]
        else:
            return []
    def getMin(self) -> int:
        return min(self.MinStack)
