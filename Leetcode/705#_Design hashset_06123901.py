class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class MyHashSet:

    def __init__(self,size=1000):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.hash = [None]*self.size        #每一個hashset都是鏈表

    def add(self, key: int) -> None:
        index = key % self.size             #求餘數，保證key有地方可以放
        n = self.hash[index]                #n記錄hashset裡面第index的數
        new = Node(key)                     #key設定為new節點
        while n :                           #如果n存在，若n的值剛好等於key值，則不放入key
            if n.val == key:
                return
            n = n.next                      #遍歷n，指向n的下一個節點
        new.next=self.hash[index]                       #如果n不存在的話，跳出迴圈，把new節點的指針指向self.hash[index]的節點
        self.hash[index] = new              #new節點複製給self.hash[index]節點
        

    def remove(self, key: int) -> None:
        index = key % self.size
        n = self.hash[index]
        if n is None:
            return False
        elif n.val==key:               #如果n存在並且n的值等於key
            self.hash[index] = n.next        #移除當前的節點，把當前節點的下一個節點續接
            return
        pre = None             #設定pre存放前一個節點   
        while n:               #如果n存在
            pre = n                 #遍歷pre。如果n的值不等於key，pre就記錄為n
            n = n.next              #遍歷n。 n走到下一個
            if n.val == key:        #若n的值等於key
                pre.next = n.next   #刪除當前的n，然後把前一節節點指向n的下一個節點
                return
        return False    
            

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = key % self.size
        n = self.hash[index]
        while n:
            if n.val == key:
                return True
            n=n.next
        return False
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
