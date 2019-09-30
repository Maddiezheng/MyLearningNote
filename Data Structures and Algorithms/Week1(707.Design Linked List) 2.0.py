class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList(object):
 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.len = 0
 
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.len:
            return -1
        
        current = self.val
        
        for i in range(0, index):            
            current = current.next
 
        return current.val
    
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)
 
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.len, val)
        
 
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.len:          
            return
        
        current = self.val
        new = Node(val)
                
        if index <= 0:
            new.next = current      #創建的node指向current
            self.val = new         #self.val的值為創建的node的val
        else:                        
            for i in range(index - 1):
                current = current.next #更新current  跑完時，current停留在index的node
            new.next = current.next#創建的Node下一個即當前node的下一個（在當前index插入newNode）
            current.next = new 
            
        self.len += 1
        
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.len:
            return
        
        current = self.val
        
        if index == 0:
            self.val = self.val.next#當前index的node被delete，則下一個node變成當前
        else:
            for i in range(0, index - 1):
                current = current.next     #更新current，下一個變成當前
            current.next = current.next.next #跑完range，當前node指向本來的node的下一個的下一個，即當前node的下一個
 
        self.len -= 1
 


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
