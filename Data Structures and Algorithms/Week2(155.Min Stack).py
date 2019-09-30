class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []                    #普通stack
        self.minStack = []                    #只放min的stack

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minStack) == 0 or x <= self.minStack[-1]:    #min的成立條件
            self.minStack.append(x)
        
    def pop(self) -> None:
        top = self.stack[-1]
        self.stack.pop()
        if top == self.minStack[-1]:         #注意不要忘記剛好pop最小值時，minStack的val
            self.minStack.pop()
        
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
