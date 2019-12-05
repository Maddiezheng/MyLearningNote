from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
        self.val = val
        self.next = None
        
class MyHashSet:
    def MyMD5(self,key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        h.hexdigest()
        int(h.hexdigest(), 16)
        return int(h.hexdigest(), 16)
        
    def __init__(self, capacity=5):
        """
        :type capacity: int
        :rtype: None
        """
        self.capacity = capacity
        self.data = [None] * capacity

    def add(self, key):
        """
        :type key: str
        :rtype: None
        """
        My_MD5 = self.MyMD5(key)
        index = My_MD5 % (self.capacity)
        n = self.data[index]   
        newnode = ListNode(My_MD5)
        
        if n is None:                   #如果n沒有東西，則把key直接加入到當前index裡
            self.data[index] = newnode
        elif n.val ==My_MD5:      #如果n和key相等，退出
            return False
        else:   #如果n和key不相等
            while n.next is not None:
                if n.next.val == My_MD5:
                    return False
                n = n.next
            n.next = newnode
        # 「!=」 比較的是數值或字串；若涉及到index，還是需要用is not None
 
    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
        My_MD5 = self.MyMD5(key)
        index = My_MD5 % (self.capacity)
        n = self.data[index]
        if n is None:
            return False
        elif n.val==My_MD5:               #如果n存在並且n的值等於key
            self.data[index] = n.next        #移除當前的節點，把當前節點的下一個節點續接
            return
        pre = None             #設定pre存放前一個節點   
        while n:               #如果n存在
            pre = n                 #遍歷pre。如果n的值不等於key，pre就記錄為n
            n = n.next              #遍歷n。 n走到下一個
            if n.val == My_MD5:        #若n的值等於key
                pre.next = n.next   #刪除當前的n，然後把前一節節點指向n的下一個節點
                return
        return False    
                
                
     
        
    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
        My_MD5 = self.MyMD5(key)
        index = My_MD5 % (self.capacity)
        n = self.data[index]
        
        while n:
            if n.val == My_MD5:
                return True
            n = n.next
        return False



#參考資料：
#https://blog.csdn.net/weixin_40449300/article/details/83590274
#https://blog.csdn.net/qweqwrqw/article/details/90448746
