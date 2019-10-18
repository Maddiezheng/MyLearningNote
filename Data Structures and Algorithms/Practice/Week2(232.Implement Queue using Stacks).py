class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack = []         #只進行進入stack的動作
        self.outStack = []        #只進行出stack和peak的動作

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inStack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.outStack:
            return self.outStack.pop()
        else:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
            return self.outStack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.outStack:
            return self.outStack[-1]
        else:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
            return self.outStack[-1]
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.inStack) == 0 and len(self.outStack) == 0        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
