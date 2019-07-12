class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        else:
            if x < self.min_stack[-1]:
                self.min_stack.append(x)
            else:
                self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class MinStackO1Space:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.last_elem = None

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(x)
            self.last_elem = x

        else:
            if x < self.last_elem:
                self.stack.append(2 * x - self.last_elem)
                self.last_elem = x
            else:
                self.stack.append(x)

    def pop(self) -> None:
        last_stack = self.stack.pop()
        if last_stack < self.last_elem:
            ret_val = self.last_elem
            self.last_elem = 2 * ret_val - last_stack
        else:
            ret_val = last_stack

        return ret_val

    def top(self) -> int:
        return max(self.stack[-1], self.last_elem)

    def getMin(self) -> int:
        return self.last_elem


if __name__ == "__main__":
    obj = MinStackO1Space()

    commands = ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
    items = [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]

    for c, i in zip(commands, items):
        if c == 'push':
            obj.push(i[0])
        elif c == 'top':
            print(obj.top())
        elif c == 'getMin':
            print(obj.getMin())
        elif c == 'pop':
            print(obj.pop())
