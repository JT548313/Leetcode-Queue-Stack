class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if x is not None:
            self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop(len(self.stack) - 1)

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        if len(self.stack) > 0:
            temp = sorted(self.stack)
            return temp[0]
        return 0

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())