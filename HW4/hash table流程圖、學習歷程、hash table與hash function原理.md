****Hash table（哈希表， 也叫散列表）：****

是根據關鍵碼值(Key value)而直接進行訪問的數據結構。也就是說，它通過把關鍵碼值映射到表中一個位置來訪問記錄，以加快查找的速度。這個映射函數叫做散列函數(hash function)，存放記錄的數組叫做散列表。如果數對p的關鍵字是k，哈希函數為f，那麼在理想情況下，p在哈希表中的位置就是f(k)。

哈希碰撞：在理想的情況下，不同的鍵會被轉換為不同的索引值，但是在有些情況下我們需要處理多個鍵被哈希到同一個索引值的情況。

**1、為什麼出現hash table？**

已知數組，查找容易，但插入、刪除困難，會消耗性能。然而鏈表雖然解決了數組插入刪除的問題，但是鏈表的查找卻又降低了性能。結合兩者的優缺點，於是便出現了，查找容易同時插入刪除容易的哈希表，時間複雜度都為o(1)。

**2、Hash table 原理**

如果所有的鍵都是整數，那麼就可以使用一個簡單的無序數組來實現：
用hash function把鍵轉換為數組索引(index)，值即為其對應的值，這樣就可以快速訪問任意鍵的值。這是對於簡單的鍵的情況，我們將其擴展到可以處理更加複雜的類型的鍵。Hash function和鍵的類型有關，對於每種類型的鍵我們都需要一個與之對應的hash function。常見hash function算法有MD5和SHA-1。

其實，hash table的本質就是一個數組。在hash table內部，我們使用桶（bucket）來保存鍵值對，我們前面所說的數組索引即為桶號，決定了給定的鍵存於散列表的哪個桶中。Hash table所擁有的桶數被稱為散列表的容量（capacity）。

現在假設我們的hash table中有M個桶，桶號為0到M-1。我們的hash function的功能就是把任意給定的key轉為[0, M-1]上的整數。我們對hash function有兩個基本要求：一是計算時間要短，二是盡可能把鍵分布在不同的桶中。對於不同類型的鍵，我們需要使用不同的hash function，這樣才能保證有比較好的散列效果。

**3、hash table存取過程**

①首先使用hash function將被查找的鍵轉換為數組的索引。

根據 key 計算出它的哈希值 hashcode。假設桶的個數為 n，那麼這個鍵值對應該放在第 (hashcode % n) 個桶中。

②如果出現哈希碰撞，則用拉鍊法或線性探測法處理哈希碰撞。

如果該桶中已經有了鍵值對，即不同的關鍵字得到同一散列地址，那麼就使用拉鍊法或者開放尋址法（線性探測法）解決衝突。

**4、拉鍊法實現的哈希表**

Hash table本質就是一個數組 ，底層是由數組+鏈表組成，數組中的每個元素都是一個鏈表，我們可以理解為「鏈表的數組」。

通過hash function，我們可以將鍵轉換為數組的索引(0-M-1)，但是對於兩個或者多個鍵具有相同索引值的情況，一種比較直接的解決辦法就是，將大小為M 的數組的每一個元素指向一個條鏈表，鏈表中的每一個節點都存儲散列值為該索引的鍵值對，這就是拉鍊法。 

在使用拉鍊法解決哈希碰撞時，每個桶其實是一個鏈表，屬於同一個箱子的所有鍵值對都會排列在鏈表中。



****Hash Function****

***1.Hash Function是什麼？***

它是一種從任何一種資料中建立小的數字「指紋」的方法。

Hash Function把訊息或資料 (key) 壓縮成摘要，使得資料量變小，將資料的格式固定下來。該函式將資料打亂混合，重新建立一個叫做 雜湊值（hash values，hash codes，hash sums，或hashes） 的指紋。這個雜湊值就當作是陣列的索引，資料就儲存在這個索引的位置中。雜湊值通常用一個短的隨機字母和數字組成的字串來代表。

***2.Hash Function的性質***


a)運算速度快

b)不可逆性： 無法從雜湊值推回原本的資料是什麼

c)如果兩個雜湊值是 不相同 的（根據同一函式），那麼這兩個雜湊值的原始輸入也是 不相同 的

d)如果兩個雜湊值是 相同 的（根據同一函式），那麼這兩個雜湊值的原始輸入 不一定 是相同的

e)衝突 (collision)：
也就是 第 2 種情況 發生時就稱為「雜湊衝突」。好的雜湊函式在輸入域中很少出現雜湊衝突。在雜湊表和資料處理中，不抑制衝突來區別資料，會使得資料庫記錄更難找到。

***3.hash function的應用***

加密

密碼雜湊函式（Cryptographic hash function），又譯為加密雜湊函式、密碼雜湊函式、加密雜湊函式，是雜湊函式的一種。它被認為是一種單向函式，也就是說極其難以由雜湊函式輸出的結果，回推輸入的資料是什麼。這種雜湊函式的輸入資料，通常被稱為訊息（message），而它的輸出結果，經常被稱為訊息摘要（message digest）或摘要（digest）。

許多重要的應用，都使用了密碼雜湊函式來實作，例如數位簽章，訊息鑑別碼

***流程圖：***
![-w80](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/hashtable1.jpeg)

![-w80](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/hashtable2.png)

![-w80](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/hashtable3.png)

****方法解釋****

***add：***

用於存取新的資料。

1.如果當前的index沒有東西，那麼直接把key放入。

2.如果當前的index的值和key相等，則不進行任何變動。

3.如果當前的index的值和key不相等，則key和下一個index的值進行比較，直到下一個index沒有值的時候放入key，或如果相等不進行任何改動。(有兩種方法，key可以放在最前面，也可以放在最後面，我在寫leetcode的時候是放在了最前面，這次作業想試一試放在最後面的做法)



**contains：**

用於檢查資料有沒有add進去。

用while迴圈遍歷，當前等於key的值，則return true，直到找到為止。

若遍歷完依舊沒有和key的值相等，則return false

***remove：****

用於刪除資料。

如果要remove的是最後一個index，那麼將不會進入while迴圈裡，所以不能對n.next進行判斷，還是要對n進行判斷。

這裡用了pre來記錄前一個的index，用意是如果當index和值和key相等的時候做remove動作，可以將當前index的前一個listnode和後一個接起來。


參考資料：

https://hackmd.io/@EW34LLeXTra2Oikg0WEQ5Q/HJln3jU_e?type=view

https://blog.csdn.net/CSDN2497242041/article/details/86618659

https://blog.csdn.net/iva_brother/article/details/82253989


```python
from Crypto.Hash import MD5
#h = MD5.new()
#h.update(key.encode("utf-8"))


```

先建立一個能夠把字串加密的function。


```python
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
        h.update(key.encode("utf-8"))           #使用utf8進行編碼
        print(h.hexdigest())                          #採用16進制
        print(int(h.hexdigest(), 16))                #把16進制轉為10進制
        return int(h.hexdigest(), 16)              
        
```


```python
MyHashSet().MyMD5("dog")
```

    06d80eb0c50b49a509b49f2424e8c805
    9097202055026264535080901219663267845





    9097202055026264535080901219663267845



由於這次事先做了老師要求在leetcode上面的題目，和這次作業特別相似，所以這次的作業做起來容易很多，也很少出現error(因為在寫leetcode的時候已經遇到並且弄懂、解決了 TAT....)

此處是add的建立過程。
這裡有一個技巧性的方法是key的index可以使用取餘數的辦法放進hashset當中。這個我自己沒有想到，是同學告訴我，我才知道可以這樣使用。


***這裡的add我採用的是不重複的做法：

1.如果當前的index沒有東西，那麼直接把key放入。

2.如果當前的index的值和key相等，則不進行任何變動。

3.如果當前的index的值和key不相等，則key和下一個index的值進行比較，直到下一個index沒有值的時候放入key，或如果相等不進行任何改動。(有兩種方法，key可以放在最前面，也可以放在最後面，我在寫leetcode的時候是放在了最前面，這次作業想試一試放在最後面的做法)



在詢問同學的過程裡，搞懂了一個自己平時一直沒有注意到的問題：
「!=」 比較的是數值或字串；若涉及到index，還是需要用is not None，因為它包括 val + index。


```python
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
        h.update(key.encode("utf-8"))           #使用utf8進行編碼
        print(h.hexdigest())                          #採用16進制
        print(int(h.hexdigest(), 16))                #把16進制轉為10進制
        return int(h.hexdigest(), 16)              
        
    def __init__(self, capacity=5):
        """
        :type capacity: int
        :rtype: None
        """
        self.capacity = capacity                 #設定size
        self.data = [None] * capacity         #建立數組

    def add(self, key):
        """
        :type key: str
        :rtype: None
        """
        My_MD5 = self.MyMD5(key)              #把key進行加密
        index = My_MD5 % (self.capacity)     #取餘數，保證能夠在數組的範圍當中。
        n = self.data[index]   
        newnode = ListNode(My_MD5)          #變數newnode記錄已經是LIstnode的key
        
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

        print(self.data)
    
        
        
        
        
        
#     def remove(self, key):
#         """
#         :type key: str
#         :rtype: None
#         """
#     def contains(self, key):
#         """
#         :type key: str
#         :rtype: bool(True or False)
#         """
       
        
```


```python
MyHashSet().add("dog")
```

    06d80eb0c50b49a509b49f2424e8c805
    9097202055026264535080901219663267845
    [<__main__.ListNode object at 0x108e17780>, None, None, None, None]



```python
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

        print(self.data)
    
        
        
        
        
        
#     def remove(self, key):
#         """
#         :type key: str
#         :rtype: None
#         """
#     def contains(self, key):
#         """
#         :type key: str
#         :rtype: bool(True or False)
#         """
       
```


```python
MyHashSet().add("dog")
```

    06d80eb0c50b49a509b49f2424e8c805
    9097202055026264535080901219663267845
    [<__main__.ListNode object at 0x10b6e0c50>, None, None, None, None]


接下來寫contains來檢查有沒有add進去。這個比較容易，只要寫while迴圈遍歷，當前等於key的值，則return true，直到找到為止。若遍歷完依舊沒有和key的值相等，則return false


```python
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

        print(self.data)
    
#     def remove(self, key):
#         """
#         :type key: str
#         :rtype: None
#         """

    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
        My_MD5 = self.MyMD5(key)
        index = My_MD5 % (self.capacity)
        n = self.data[index]
        
        while n:                                     #當n存在
            if n.val == My_MD5:                      #n的值與key相等
                return True
            n = n.next                                    #遍歷n，直到index到最後，若沒有值與key相等，則return false
        return False
        
        
```

發現這裡增加pig，第零個位置是None，按理來說應該是add了dog才對。猜想沒有return的緣故


```python
MyHashSet().add("dog")
MyHashSet().add("pig")
```

    [<__main__.ListNode object at 0x108eb1978>, None, None, None, None]
    [None, None, <__main__.ListNode object at 0x108eb1978>, None, None]



```python
MyHashSet().add("dog")
MyHashSet().add("dog")
```

    [<__main__.ListNode object at 0x108eb1a20>, None, None, None, None]
    [<__main__.ListNode object at 0x108eb1a20>, None, None, None, None]


然後發現一個問題，__init__裡面的self.data = [None] * capacity每一次都會被執行，所以每一次的self.data都是空的

但是後來用了助教的測資範例的程式碼，才發現沒有這個問題 TAT....
怎麼回事...有點奇怪....


```python
hashSet = MyHashSet()
hashSet.add("dog")
hashSet.add("dog")
hashSet.contains("dog")
```

    [<__main__.ListNode object at 0x108eb1cf8>, None, None, None, None]





    True



add和contains已經沒有問題了。繼續寫remove
和add的code有點類似。
remove的做法：
1.先要考慮當前index有沒有東西，沒有的話，說明不存在key
2.如果當前index有東西，並且和key相等的話，直接刪除當前的listnode。續接當前節點的下一個節點。


```python
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

        print(self.data)

        
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
        elif n.val == My_MD5:            
            self.data[index] = n.next
        else:
            while n.next is not None:
                if n.next.val == My_MD5:
                    n.next = n.next.next
                n = n.next
            return False
                
                
     
        
    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
        My_MD5 = self.MyMD5(key)
        index = My_MD5 % (self.capacity)
        n = self.data[index]
        
        while n:                                     #當n存在
            if n.val == My_MD5:                      #n的值與key相等
                return True
            n = n.next                                    #遍歷n，直到index到最後，若沒有值與key相等，則return false
        return False
        
```


```python
hashSet = MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel = hashSet.contains("pig")
print(rel)
rel = hashSet.contains("dog")
print(rel)
rel = hashSet.contains("cat")
print(rel)
hashSet.add("bird")
rel = hashSet.contains("bird")
print(rel)
hashSet.remove("pig")
rel = hashSet.contains("pig")
print(rel)
```

    [<__main__.ListNode object at 0x10b6f6588>, None, None, None, None]
    [<__main__.ListNode object at 0x10b6f6588>, None, <__main__.ListNode object at 0x10b6f64e0>, None, None]
    True
    True
    False
    [<__main__.ListNode object at 0x10b6f6588>, None, <__main__.ListNode object at 0x10b6f64e0>, None, <__main__.ListNode object at 0x10b6fa978>]
    True
    False


想了一下剛剛那種remove的做法，如果要remove的是最後一個index，那麼將不會進入while迴圈裡，所以不能對n.next進行判斷，還是要對n進行判斷。
這裡用了pre來記錄前一個的index，用意是如果當index和值和key相等的時候做remove動作，可以將當前index的前一個listnode和後一個接起來。


```python
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

        print(self.data)

        
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
```


```python
hashSet = MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel = hashSet.contains("pig")
print(rel)
rel = hashSet.contains("dog")
print(rel)
rel = hashSet.contains("cat")
print(rel)
hashSet.add("bird")
rel = hashSet.contains("bird")
print(rel)
hashSet.remove("pig")
rel = hashSet.contains("pig")
print(rel)
```

    [<__main__.ListNode object at 0x109301470>, None, None, None, None]
    [<__main__.ListNode object at 0x109301470>, None, <__main__.ListNode object at 0x109301710>, None, None]
    True
    True
    False
    [<__main__.ListNode object at 0x109301470>, None, <__main__.ListNode object at 0x109301710>, None, <__main__.ListNode object at 0x10b6f6ef0>]
    True
    False


和助教的測試結果範例最後跑出的結果相同。


```python

```
