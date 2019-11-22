
BST原理：

「二元搜尋樹」(Binary Search Trees)是一棵二元樹，在這基礎上它或者是一棵空樹；或者是具有下列性質的二元樹：

（1）若左子樹不空，則左子樹上所有結點的值均小於它的根結點的值； 

（2）若右子樹不空，則右子樹上所有結點的值均大於它的根結點的值； 

（3）左、右子樹也分別為二元查找樹

它的功能有很多，例如新增、查找、刪除、修正等。




參考資料：

https://blog.csdn.net/ShyTan/article/details/80984582
https://www.csie.ntu.edu.tw/~r95116/CA200/slide/C10_Tree.pdf

一開始邏輯上還是有錯誤


```
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None
       
    
class Solution(object):
    def __init__(self):
        self.root = None
        
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if self.root == None:
            self.root =TreeNode(val)
        if val > root.val:
            if root.right:
                return Solution().insert(root.right, val)
            else:
                root.right = TreeNode(val)
        else:
            if root.left:
                return Solution().insert(root.left,val)
            else:
                root.left = TreeNode(val)
                
    
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution()
print(a.insert(root1,4)==root1.left.right)

```

    False


然後發現缺少相等的條件


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None
       
    
class Solution(object):
    def __init__(self):
        self.root = None
        
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if self.root == None:
            self.root =TreeNode(val)
            
        if val == root.val:                          #考慮重複值的insert，把它insert到離root最近的地方
            SameNode = TreeNode(val)       #創建重複值的節點
            SameNode.left = root.left          #重複值的左指針指向原本root的左節點
            root.left = SameNode               #現在的root的左節點指向重複值節點
            return   SameNode
        
        elif val>root.val:
            if root.right:
                return Solution().insert(root.right, val)
            else:
                root.right = TreeNode(val)
        else:
            if root.left:
                return Solution().insert(root.left,val)
            else:
                root.left = TreeNode(val)
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution()
print(a.insert(root1,4)==root1.left.right)
```

    False


測試過邏輯上是沒有問題，但是最後的判斷是錯誤的。檢查發現自己沒有return root.right 和root.left


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None
       
    
class Solution(object):
    def __init__(self):
        self.root = None
        
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if self.root == None:
            self.root =TreeNode(val)
            
        if val == root.val:                          #考慮重複值的insert，把它insert到離root最近的地方
            SameNode = TreeNode(val)       #創建重複值的節點
            SameNode.left = root.left          #重複值的左指針指向原本root的左節點
            root.left = SameNode               #現在的root的左節點指向重複值節點
            return   SameNode
        
        elif val>root.val:
            if root.right:
                return Solution().insert(root.right, val)
            else:
                root.right = TreeNode(val)
                return root.right
        else:
            if root.left:
                return Solution().insert(root.left,val)
            else:
                root.left = TreeNode(val)
                return root.left
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution()
print(a.insert(root1,4)==root1.left.right)
```

    True


這部分寫search的function

想了一下不是回傳index，應該是回傳node，然後這裡index的表示也是錯的，正確寫法是list.index。但這裡不適用


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return index(root)
        
        if target > root.val:
            if target > root.right:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        else:
            if target > root.left:
                if target > root.left:
                    return Solution().search(root.right,target)
                else:
                    return Solution().search(root.left,target)
        return index(root)
                
            
        
    
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution()
print(a.search(root1,5)==root1.val)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-32-1799d97a680c> in <module>()
          8 root1.right.left.left = TreeNode(6)
          9 a = Solution()
    ---> 10 print(a.search(root1,5)==root1.val)
    

    <ipython-input-30-022ab4f4693e> in search(self, root, target)
         18         """
         19         if target == root.val:
    ---> 20             return index(root)
         21 
         22         if target > root.val:


    NameError: name 'index' is not defined



```
應該search到之後，回傳這個節點。目前可以測試出存在的節點的查找，但是如果不存在的節點，查找的時候會被告知是空元素，沒有對應的屬性。
```


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        elif target > root.val:
            return Solution().search(root.right,target)
        else:
            return Solution().search(root.left,target)
        
            
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution()
print(a.search(root1,7)==root1.right.left)
```

    True



```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution()
print(a.search(root1,9)==None)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-45-0821b931dad5> in <module>()
          8 root1.right.left.left = TreeNode(6)
          9 a = Solution()
    ---> 10 print(a.search(root1,9)==None)
    

    <ipython-input-42-f874f6d7c26f> in search(self, root, target)
         20             return root
         21         elif target > root.val:
    ---> 22             return Solution().search(root.right,target)
         23         else:
         24             return Solution().search(root.left,target)


    <ipython-input-42-f874f6d7c26f> in search(self, root, target)
         20             return root
         21         elif target > root.val:
    ---> 22             return Solution().search(root.right,target)
         23         else:
         24             return Solution().search(root.left,target)


    <ipython-input-42-f874f6d7c26f> in search(self, root, target)
         22             return Solution().search(root.right,target)
         23         else:
    ---> 24             return Solution().search(root.left,target)
         25 
         26 


    <ipython-input-42-f874f6d7c26f> in search(self, root, target)
         17         :rtype: TreeNode(searched node)
         18         """
    ---> 19         if target == root.val:
         20             return root
         21         elif target > root.val:


    AttributeError: 'NoneType' object has no attribute 'val'



```
增加了while迴圈，如果target和節點在比較的時候，比到葉節點都沒有元素和他相等的話，就回傳None。
```


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        while root.right and root.left:
            if target == root.val:
                return root
            elif target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution()
print(a.search(root1,7)==root1.right.left)
```

    False



```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution()
print(a.search(root1,9)==None)
```

    True



```
測試的時候還是會被判斷有一個節點是False，檢查了一下，不能寫左右節點都存在，只要有一個存在就可以了
```


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        while root.right or root.left:
            if target == root.val:
                return root
            elif target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution()
print(a.search(root1,6)==root1.right.left.left)
```

    False



```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution()
print(a.search(root1,7)==root1.right.left)
```

    True



```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution()
print(a.search(root1,9)==None)
```

    True


測試了一下查詢葉節點，發現這個while迴圈還是有個小問題。如果比到葉節點的上一個節點，判斷這個節點的下一個節點(即葉節點)有沒有左右節點，這時會馬上跳開循環，這樣最後一個葉節點沒有被比較就已經中止了迴圈。
所以應該是先比較當前節點和target，然後再判斷當前節點有沒有左右節點。


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
        
                
            
                
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution()
print(a.search(root1,6)==root1.right.left.left)


```

    True



```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution()
print(a.search(root1,6)==root1.right.left.left)
```

    True



```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution()
print(a.search(root1,7)==root1.right.left)
```

    True



```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution()
print(a.search(root1,9)==None)
```

    True



```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution()
p=a.search(root1,7)
p
```




    <__main__.TreeNode at 0x103f24c18>



接下來寫delete。
從大方向看，有不重複和重複的兩個方向。
從小方向看，分三種情況：
1.target是葉子節點，

先寫沒有重複的狀況。


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if target == root.val:                     #如果要刪去的是根節點
            if root.left == None and root.right: #如果根節點的左節點不存在
                root = root.right                                                          #root節點變為root.right節點
                root.right = root.right.right                                           #重新調整root的右指針
                root.left = root.right.left                                              #重新調整root的左指針
            elif root.right == None and root.left:   #如果根節點的右節點不存在
                root = root.left
                root.left = root.left.left
                root.right = root.left.right
            else:                                              #如果根節點的左右節點都存在
                if root.left.right:                          #如果根節點的左節點有右子樹
                    root = root.left.right
                    root.left = root.left
                else:                                         #如果根節點的左節點無右子樹
                    root = root.left                       #root節點變為root.left的節點
                    root.left = root.left.left
                    root.right = root.right
                    
    
                
            
            
        
```


```
 p = Solution().search(root,target)    #此處會告知查找到的節點是哪一個
        if p.left == None and p.right:
            p = p.right
            p.right = p.right.right
                
```


```
"root1 = TreeNode(10)
"root1.right= TreeNode(20)
"root1.right.right = TreeNode(30)
"root1.right.right.left = TreeNode(25)
"root1.right.right.right = TreeNode(35)
"Solution().delete(root1,10)
"print(root1.val ==30 and root1.left == 25 and root1.right == 35)
```


      File "<ipython-input-98-32dff7ee78cb>", line 7
        print(root1.val ==30 and root1.left == 25 and root1.right == 35)"
                                                                         ^
    SyntaxError: EOL while scanning string literal




```
root1 = TreeNode(10)
root1.right = TreeNode(30)
root1.right.left = TreeNode(25)
root1.right.right = TreeNode(35)
Solution().delete(root1,10)
print(root1.val ==30 and root1.left == 25 and root1.right == 35)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-99-db598ee38be5> in <module>()
          3 root1.right.left = TreeNode(25)
          4 root1.right.right = TreeNode(35)
    ----> 5 Solution().delete(root1,10)
          6 print(root1.val ==30 and root1.left == 25 and root1.right == 35)


    <ipython-input-95-59164003dd14> in delete(self, root, target)
         21                 root = root.right                                                          #root節點變為root.right節點
         22                 root.right = root.right.right                                           #重新調整root的右指針
    ---> 23                 root.left = root.right.left                                              #重新調整root的左指針
         24             elif root.right == None and root.left:   #如果根節點的右節點不存在
         25                 root = root.left


    AttributeError: 'NoneType' object has no attribute 'left'



```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if target == root.val:                     #如果要刪去的是根節點
            if root.left == None and root.right: #如果根節點的左節點不存在
                root = root.right                                                          #root節點變為root.right節點
                root.right = root.right.right                                           #重新調整root的右指針
                root.left = root.right.left                                              #重新調整root的左指針
                return root, root.right, root.left
            elif root.right == None and root.left:   #如果根節點的右節點不存在
                root = root.left
                root.left = root.left.left
                root.right = root.left.right
                return root, root.right, root.left
            else:                                              #如果根節點的左右節點都存在
                if root.left.right:                          #如果根節點的左節點有右子樹
                    root = root.left.right
                    root.left = root.left
                    return root, root.left
                else:                                         #如果根節點的左節點無右子樹
                    root = root.left                       #root節點變為root.left的節點
                    root.left = root.left.left
                    root.right = root.right
                    return root, root.right
                    
    
                    
```

又被提醒是空元素，沒有對應的屬性值


```
root1 = TreeNode(10)
root1.right = TreeNode(30)
root1.right.left = TreeNode(25)
root1.right.right = TreeNode(35)
Solution().delete(root1,10)
print(root1.val ==30 and root1.left == 25 and root1.right == 35)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-108-db598ee38be5> in <module>()
          3 root1.right.left = TreeNode(25)
          4 root1.right.right = TreeNode(35)
    ----> 5 Solution().delete(root1,10)
          6 print(root1.val ==30 and root1.left == 25 and root1.right == 35)


    <ipython-input-107-c61116a3ebd7> in delete(self, root, target)
         21                 root = root.right                                                          #root節點變為root.right節點
         22                 root.right = root.right.right                                           #重新調整root的右指針
    ---> 23                 root.left = root.right.left                                              #重新調整root的左指針
         24                 return root, root.right, root.left
         25             elif root.right == None and root.left:   #如果根節點的右節點不存在


    AttributeError: 'NoneType' object has no attribute 'left'



```
檢查之後發現根本沒有實現原本樹的delete
```


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if target == root.val:                     #如果要刪去的是根節點
            if root.left == None: #如果根節點的左節點不存在
                root = root.right   #root節點變為root.right節點
                root.right = root.right.right                                           #重新調整root的右指針
                root.left = root.right.left                                              #重新調整root的左指針
                return root, root.right, root.left
```


```
root1 = TreeNode(10)
root1.right = TreeNode(30)
root1.left = TreeNode(None)
root1.right.left = TreeNode(25)
root1.right.right = TreeNode(35)
Solution().delete(root1,10)
print(root1.val)
```

    10


然後重新看了一下code，發現重新調整root的左右指針時，有些問題。然後想起來之前做linked list的時候，會對進行賦值，來時間指針的更新


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if target == root.val:                     #如果要刪去的是根節點
            if root.left == None: #如果根節點的左節點不存在
                cur = root
                root = root.right   #root節點變為root.right節點
                root.val = root.right.val
                root.right = cur.right.right                                           #重新調整root的右指針
                root.right.val = cur.right.right.val
                root.left = cur.right.left                                              #重新調整root的左指針
                root.left.val = cur.right.left.val
                return root, root.right, root.left
```


```
root1 = TreeNode(10)
root1.right = TreeNode(30)
root1.left = TreeNode(None)
root1.right.left = TreeNode(25)
root1.right.right = TreeNode(35)
Solution().delete(root1,10)
print(root1.left.val)
```

    None



```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if target == root.val:                     #如果要刪去的是根節點
            if root.left == None: #如果根節點的左節點不存在
                cur = root
                root = root.right   #root節點變為root.right節點
                root.right = cur.right.right                                           #重新調整root的右指針
                root.left = cur.right.left                                              #重新調整root的左指針
                return root, root.right, root.left
```


```
root1 = TreeNode(10)
root1.right = TreeNode(30)
root1.right.left = TreeNode(25)
root1.right.right = TreeNode(35)
Solution().delete(root1,10)
print(root1.left.val)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-153-48e78b60b29d> in <module>()
          4 root1.right.right = TreeNode(35)
          5 Solution().delete(root1,10)
    ----> 6 print(root1.left.val)
    

    AttributeError: 'NoneType' object has no attribute 'val'



```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if target > root.val:
            return Solution().delete(root.right,target)
        elif target < root.val:
            return Solution().delete(root.left.target)
        else: 
            return root
        
        if root.left == None:
            root = root.right
        elif root.right == None:
            root = root.left
        else:                  
            pre = root                #cur為被刪除節點的前一個節點
            cur = root.left           #curl為被刪除的節點
            while curl.right:        #
                pre = curl.right
                curl.right = 
            
```


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if target > root.val:
            root.left = Solution().delete(root.right,target)
        elif target < root.val:
            root.right =  Solution().delete(root.left.target)
        else: 
            if root.left and root.right:
                minnode = root.right
```

寫到這裡發現查找最小值需要再寫一個函數來輔助


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None
        
class Solution(object):
    def FindMin(self,root):
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution()
print(a.FindMin(root1)==root1.left.left.left)
```

    True



```
然後再回到剛剛寫delete的function，在裡面遞迴FindMin函數，找到右子樹的最小值
```


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
        
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if target > root.val:
            root.right = Solution().delete(root.right,target)
        elif target < root.val:
            root.left =  Solution().delete(root.left.target)
        else: 
            if root.left and root.right:                                 #如果左右子樹都存在的話
                minnode = Solution().FindMin(root.right)
                root.val = minnode.val                                       #把刪除節點用找到的最小值替代
                root.right = Solution().delete(root,root.right.val)    #把替換節點從樹中刪除
            elif root.left:                                                  #只有左子樹
                root = root.left
            elif root.right:                                                #只有右子樹
                root = root.right
            else:                                                            #？？？左右子樹都不存在，即葉子節點。直接命其父節點
                root.left == None
                root.right == None
        return root
                
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
Solution().delete(root1,8)
print(root1.val==5 and root1.left.val==3 and root1.left.left.val==3 and root1.left.left.left.val==-5)
print(root1.right.val == 10 and root1.right.left.val ==7 and root1.right.left.left.val ==6)
```


    ---------------------------------------------------------------------------

    RecursionError                            Traceback (most recent call last)

    <ipython-input-183-b3ce6251aecd> in <module>()
          7 root1.right.left = TreeNode(7)
          8 root1.right.left.left = TreeNode(6)
    ----> 9 Solution().delete(root1,8)
         10 print(root1.val==5 and root1.left.val==3 and root1.left.left.val==3 and root1.left.left.left.val==-5)
         11 print(root1.right.val == 10 and root1.right.left.val ==7 and root1.right.left.left.val ==6)


    <ipython-input-182-336c28fbd552> in delete(self, root, target)
         25         """
         26         if target > root.val:
    ---> 27             root.right = Solution().delete(root.right,target)
         28         elif target < root.val:
         29             root.left =  Solution().delete(root.left.target)


    <ipython-input-182-336c28fbd552> in delete(self, root, target)
         33                 root.val = minnode.val                                       #把刪除節點用找到的最小值替代
         34 
    ---> 35                 root.right = Solution().delete(root,root.right.val)    #把替換節點從樹中刪除
         36             elif root.left:                                                  #只有左子樹
         37                 root = root.left


    ... last 1 frames repeated, from the frame below ...


    <ipython-input-182-336c28fbd552> in delete(self, root, target)
         33                 root.val = minnode.val                                       #把刪除節點用找到的最小值替代
         34 
    ---> 35                 root.right = Solution().delete(root,root.right.val)    #把替換節點從樹中刪除
         36             elif root.left:                                                  #只有左子樹
         37                 root = root.left


    RecursionError: maximum recursion depth exceeded in comparison



```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
        
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if target > root.val:
            root.right = Solution().delete(root.right,target)
            return root
        elif target < root.val:
            root.left =  Solution().delete(root.left.target)
            return root
        else: 
            p = root
            if p.left == None :
                root = p.right 
                return root
            elif p.right == None:
                root = p.left
                return root
            else: #左右節點都存在
                minnode = Solution().FindMin(root.right)
                root = minnode                                      #把刪除節點用找到的最小值替代
                minnode.right = Solution().delete(root,root.right.val)    #把替換節點從樹中刪除
                minnode.left = root.left
                return minnode
                    
                
                    
                
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
Solution().delete(root1,8)
print(root1.val==5 and root1.left.val==3 and root1.left.left.val==3 and root1.left.left.left.val==-5)
print(root1.right.val == 10 and root1.right.left.val ==7 and root1.right.left.left.val ==6)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-187-b3ce6251aecd> in <module>()
          7 root1.right.left = TreeNode(7)
          8 root1.right.left.left = TreeNode(6)
    ----> 9 Solution().delete(root1,8)
         10 print(root1.val==5 and root1.left.val==3 and root1.left.left.val==3 and root1.left.left.left.val==-5)
         11 print(root1.right.val == 10 and root1.right.left.val ==7 and root1.right.left.left.val ==6)


    <ipython-input-186-a66d063dc6a1> in delete(self, root, target)
         25         """
         26         if target > root.val:
    ---> 27             root.right = Solution().delete(root.right,target)
         28             return root
         29         elif target < root.val:


    <ipython-input-186-a66d063dc6a1> in delete(self, root, target)
         41                 minnode = Solution().FindMin(root.right)
         42                 root = minnode                                      #把刪除節點用找到的最小值替代
    ---> 43                 minnode.right = Solution().delete(root,root.right.val)    #把替換節點從樹中刪除
         44                 minnode.left = root.left
         45                 return minnode


    AttributeError: 'NoneType' object has no attribute 'val'



```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
        
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if target == root.val:                        #當刪去的節點是根節點時
            if root.right == None and root.left:                      #當根節點只有左節點時
                root = root.left
             
            elif root.left == None and root.right:                   #當根節點只有右節點時
                root = root.right
                
            elif root.right == None and root.left == None:     #當根節點沒有左右節點，即樹裡只有根節點
                root = None
                
            else:                                                              #當根節點左右兩點都有時
                p = root.right                                                      #
                while p.left:                                                #
                    parent = p
                    p = p.left
                if p.right:
                    q = p.right
                    parent.left = q
                root = p
            return root
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution().delete(root1,5)
print(a.val==6 and a.left.val==3 and a.left.left.val==3 and a.left.left.left.val==-5)
print(Solution().delete(root1,5).right.val == 8 and Solution().delete(root1,5).right.left.val ==7 and Solution().delete(root1,5).right.right.val ==10)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-2-4995a94cf0b9> in <module>()
          8 root1.right.left.left = TreeNode(6)
          9 a = Solution().delete(root1,5)
    ---> 10 print(a.val==6 and a.left.val==3 and a.left.left.val==3 and a.left.left.left.val==-5)
         11 print(Solution().delete(root1,5).right.val == 8 and Solution().delete(root1,5).right.left.val ==7 and Solution().delete(root1,5).right.right.val ==10)


    AttributeError: 'NoneType' object has no attribute 'val'



```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
        
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if target == root.val:                        #當刪去的節點是根節點時
            if root.right == None and root.left:                      #當根節點只有左節點時
                root = root.left
                return root
            elif root.left == None and root.right:                   #當根節點只有右節點時
                root = root.right
                return root
            elif root.right == None and root.left == None:     #當根節點沒有左右節點，即樹裡只有根節點
                root = None
                return root
            else:                                                              #當根節點左右兩點都有時
                p = root.right                                                      #
                while p.left:                                                #
                    parent = p
                    p = p.left
                if p.right:
                    q = p.right
                    parent.left = q
                p.left = root.left
                p.right = root.right
                root = None
                return p
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution().delete(root1,5)

print(a.val)
print(a.left.val)
print(a.left.left.val)
print(a.left.left.left.val)
print(a.right.val)
print(a.right.left.val)
print(a.right.left.left.val)
print(a.right.right.val)
#print(a.val==6 and a.left.val==3 and a.left.left.val==3 and a.left.left.left.val==-5)
#print(Solution().delete(root1,5).right.val == 8 and Solution().delete(root1,5).right.left.val ==7 and Solution().delete(root1,5).right.right.val ==10)
```

    6
    3
    3
    -5
    8
    7
    6
    10


然後再寫當target不在根節點的狀況。然後run的時候發現root.val是delete的當前節點的BST，所以問題應該是出在return。並且發現如果用最小值替換delete值，把deletenode刪去的時候，還要考慮parent的指針重新更新。找parant太麻煩，於是我想到可以把找到的最小值節點的值複製給delete node，然後只要把最小值節點刪掉即可，這樣比較方便的是，不用再考慮delete node的parant node的pointer，只要考慮最小值節點的parent的pointer即可。


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if target == root.val:                        #當刪去的節點是根節點時
            if root.right == None and root.left:                      #當根節點只有左節點時
                root = root.left
                return root
            elif root.left == None and root.right:                   #當根節點只有右節點時
                root = root.right
                return root
            elif root.right == None and root.left == None:     #當根節點沒有左右節點，即樹裡只有根節點
                root = None
                return root
            else:                                                              #當根節點左右兩點都有時
                p = root.right                                                      #選擇尋找右子樹的最小值
                while p.left:                                                         #找最小值，直到找到最小值，跳出迴圈
                    parent = p                                                      #記錄父節點的位置
                    p = p.left                                                        #走到下一個左節點
                if p.right:                                                    #如果最小值存在右節點
                    q = p.right
                    parent.left = q                                        #parent指向替換值的右節點
                p.left = root.left  #p是找到的最小值，替換根節點。則p的左指針指向原本根節點的左邊
                p.right = root.right  #p的右指針指向本來的根節點的右邊
                root = None       #刪掉根節點
                return p             #要記得回傳p的值
        else:                                               #當刪去的節點不是根節點時，即target != root.val
            delnode = Solution().search(root,target)            #找到要刪去的節點，記為delnode
            if delnode.right == None and delnode.left:             #當要刪去節點只有左節點時
                d = delnode.left
                delnode.val = d.val                                                #把左節點的值賦給要刪去的節點
                return delnode
                if d.left:                                                               #如果左節點還存在左節點
                    delnode.left = d.left                                          #要刪去的節點的左指針指向左節點的左節點 
                    return delnode.left
                if d.right:                                                             #如果左節點存在右節點
                    delnode.right = d.right                                      #要刪去的節點的右指針指向左節點的右節點
                    return delnode.right
                delnode.left = None                                     #刪去要刪去節點的左節點(因為左節點已經替換的原要刪去的節點)
            elif delnode.left == None and delnode.right:
                d = delnode.right 
                delnode.val = d.val
                return delnode
                if d.left:
                    delnode.left = d.left
                    return delnode.left
                if d.right:
                    delnode.right = d.right
                    return delnode.right
                delnode.right  = None
            elif delnode.left == None and delnode.right == None:   #如果要刪去節點沒有左右節點，即要刪去節點為葉節點
                delnode = None                                                        #直接刪去要刪去的節點
            else:                                                             #要刪去節點有左右節點
                p = delnode.right                                   
                while p.left:                                                      #如果要刪去節點的右節點存在左節點，找出最小值
                    parent = p
                    p = p.left
                if p.right:                                                         #如果
                    q=p.right
                    parent.left = q
                p.left = delnode.left
                p.right = delnode.right
                delnode = None
                return p
            
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution().delete(root1,8)
print(a.val)
#print(a.right.val == 8 and a.right.left.val ==7 and a.right.left.left.val ==6)
```

    10


更改之後的版本就能跑出來了


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if target == root.val:                        #當刪去的節點是根節點時
            if root.right == None and root.left:                      #當根節點只有左節點時
                root = root.left
                return root
            elif root.left == None and root.right:                   #當根節點只有右節點時
                root = root.right
                return root
            elif root.right == None and root.left == None:     #當根節點沒有左右節點，即樹裡只有根節點
                root = None
                return root
            else:                                                              #當根節點左右兩點都有時
                p = root.right                                                      #選擇尋找右子樹的最小值
                while p.left:                                                         #找最小值，直到找到最小值，跳出迴圈
                    parent = p                                                      #記錄父節點的位置
                    p = p.left                                                        #走到下一個左節點
                if p.right:                                                    #如果最小值存在右節點
                    q = p.right
                    parent.left = q                                        #parent指向替換值的右節點
                p.left = root.left  #p是找到的最小值，替換根節點。則p的左指針指向原本根節點的左邊
                p.right = root.right  #p的右指針指向本來的根節點的右邊
                root = None       #刪掉根節點
                return p             #要記得回傳p的值
        else:                                               #當刪去的節點不是根節點時，即target != root.val
            delnode = Solution().search(root,target)            #找到要刪去的節點，記為delnode
            if delnode.right == None and delnode.left:             #當要刪去節點只有左節點時
                d = delnode.left
                delnode.val = d.val                                                #把左節點的值賦給要刪去的節點
                return delnode
                if d.left:                                                               #如果左節點還存在左節點
                    delnode.left = d.left                                          #要刪去的節點的左指針指向左節點的左節點 
                    return delnode.left
                if d.right:                                                             #如果左節點存在右節點
                    delnode.right = d.right                                      #要刪去的節點的右指針指向左節點的右節點
                    return delnode.right
                delnode.left = None                                     #刪去要刪去節點的左節點(因為左節點已經替換的原要刪去的節點)
            elif delnode.left == None and delnode.right:
                d = delnode.right 
                delnode.val = d.val
                return delnode
                if d.left:
                    delnode.left = d.left
                    return delnode.left
                if d.right:
                    delnode.right = d.right
                    return delnode.right
                delnode.right  = None
            elif delnode.left == None and delnode.right == None:   #如果要刪去節點沒有左右節點，即要刪去節點為葉節點
                delnode = None                                                        #直接刪去要刪去的節點
            else:                                                             #要刪去節點有左右節點
                p = delnode.right                                   
                while p.left:                                                      #如果要刪去節點的右節點存在左節點，找出最小值
                    parent = p
                    p = p.left
                delnode.val = p.val                                           #把最小值的值複製給要刪除的節點
                if p.right:                                                        #如果最小值存在右節點
                    q=p.right                                                    
                    parent.left = q                                             #把刪去節點的父節點指向刪去節點的右節點
                p = None                                                        #刪除最小節點
                return root
           
            
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution().delete(root1,8)
print(a.val)
print(a.left.val)
print(a.left.left.val)
print(a.left.left.left.val)
print(a.right.val)
print(a.right.left.val)
print(a.right.left.left.val)
print(a.right.right.val)
#print(a.right.val == 8 and a.right.left.val ==7 and a.right.left.left.val ==6)
```

    5
    3
    3
    -5
    8
    7
    6
    10


以上是BST裡面沒有重複值的狀況。接下來想一下有重複值的情況該怎麼遍歷。


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        i = 0
        while Solution().search(root,target) != None:
            root = root.left
            i += 1
        return i
            
        while i > 0:
            if target == root.val:                        #當刪去的節點是根節點時
                if root.right == None and root.left:                      #當根節點只有左節點時
                    root = root.left
                    return root
                elif root.left == None and root.right:                   #當根節點只有右節點時
                    root = root.right
                    return root
                elif root.right == None and root.left == None:     #當根節點沒有左右節點，即樹裡只有根節點
                    root = None
                    return root
                else:                                                              #當根節點左右兩點都有時
                    p = root.right                                                      #選擇尋找右子樹的最小值
                    while p.left:                                                         #找最小值，直到找到最小值，跳出迴圈
                        parent = p                                                      #記錄父節點的位置
                        p = p.left                                                        #走到下一個左節點
                    if p.right:                                                    #如果最小值存在右節點
                        q = p.right
                        parent.left = q                                        #parent指向替換值的右節點
                    p.left = root.left  #p是找到的最小值，替換根節點。則p的左指針指向原本根節點的左邊
                    p.right = root.right  #p的右指針指向本來的根節點的右邊
                    root = None       #刪掉根節點
                    return p             #要記得回傳p的值
            else:                                               #當刪去的節點不是根節點時，即target != root.val
                delnode = Solution().search(root,target)            #找到要刪去的節點，記為delnode
                if delnode.right == None and delnode.left:             #當要刪去節點只有左節點時
                    d = delnode.left
                    delnode.val = d.val                                                #把左節點的值賦給要刪去的節點
                    return delnode
                    if d.left:                                                               #如果左節點還存在左節點
                        delnode.left = d.left                                          #要刪去的節點的左指針指向左節點的左節點 
                        return delnode.left
                    if d.right:                                                             #如果左節點存在右節點
                        delnode.right = d.right                                      #要刪去的節點的右指針指向左節點的右節點
                        return delnode.right
                    delnode.left = None                                     #刪去要刪去節點的左節點(因為左節點已經替換的原要刪去的節點)
                elif delnode.left == None and delnode.right:
                    d = delnode.right 
                    delnode.val = d.val
                    return delnode
                    if d.left:
                        delnode.left = d.left
                        return delnode.left
                    if d.right:
                        delnode.right = d.right
                        return delnode.right
                    delnode.right  = None
                elif delnode.left == None and delnode.right == None:   #如果要刪去節點沒有左右節點，即要刪去節點為葉節點
                    delnode = None                                                        #直接刪去要刪去的節點
                else:                                                             #要刪去節點有左右節點
                    p = delnode.right                                   
                    while p.left:                                                      #如果要刪去節點的右節點存在左節點，找出最小值
                        parent = p
                        p = p.left
                    delnode.val = p.val                                           #把最小值的值複製給要刪除的節點
                    if p.right:                                                        #如果最小值存在右節點
                        q=p.right                                                    
                        parent.left = q                                             #把刪去節點的父節點指向刪去節點的右節點
                    p = None                                                        #刪除最小節點
                    return root
            i -= 1
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution().delete(root1,3)
a
print(a.val)
#print(a.left.val)
#print(a.left.left.val)
#print(a.left.left.left.val)
#print(a.right.val)
#print(a.right.left.val)
#print(a.right.left.left.val)
#print(a.right.val == 8 and a.right.left.val ==7 and a.right.left.left.val ==6)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-61-67081e4f5a5c> in <module>()
          9 a = Solution().delete(root1,3)
         10 a
    ---> 11 print(a.val)
         12 #print(a.left.val)
         13 #print(a.left.left.val)


    AttributeError: 'int' object has no attribute 'val'



```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        i = 0
        while Solution().search(root,target) != None:
            root = root.left
            i += 1
        return i
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution().search(root1.left,3)
print(a)
```

    <__main__.TreeNode object at 0x103c444a8>



```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if target == root.val:                        #當刪去的節點是根節點時
            n = root                                             #考慮重複的狀況
            while n.left.val == target and n.left :
                n = n.left
            root.left = n.left
                
            if root.right == None and root.left:                      #當根節點只有左節點時
                root = root.left
                return root
            elif root.left == None and root.right:                   #當根節點只有右節點時
                root = root.right
                return root
            elif root.right == None and root.left == None:     #當根節點沒有左右節點，即樹裡只有根節點
                root = None
                return root
            else:                                                              #當根節點左右兩點都有時
                p = root.right                                                      #選擇尋找右子樹的最小值
                while p.left:                                                         #找最小值，直到找到最小值，跳出迴圈
                    parent = p                                                      #記錄父節點的位置
                    p = p.left                                                        #走到下一個左節點
                root.val = p.val
                if p.right:                                                    #如果最小值存在右節點
                    q = p.right
                    parent.left = q                                        #parent指向替換值的右節點
                p = None       #刪掉根節點
                return root             #要記得回傳p的值
        else:                                               #當刪去的節點不是根節點時，即target != root.val
            delnode = Solution().search(root,target)            #找到要刪去的節點，記為delnode
            d = delnode
            q = d.left
            while q == target and q:        #如果刪去的節點的左節點和刪去的值相等，且該左節點存在
                d.val = q.val                            #把刪去節點的左節點的值複製給刪去節點
                if q.left:                                  #如果刪去節點的左節點存在自己的左節點
                    q = q.left                               #把刪去節點的左節點指向「刪去節點的左節點存在自己的左節點」
                d.left = None                             #把刪去節點的左節點刪除
            #直到重複值不再出現
            
            if delnode.right == None and delnode.left:             #當要刪去節點只有左節點時
                d = delnode.left
                delnode.val = d.val                                                #把左節點的值賦給要刪去的節點
                return delnode
                if d.left:                                                               #如果左節點還存在左節點
                    delnode.left = d.left                                          #要刪去的節點的左指針指向左節點的左節點 
                    return delnode.left
                if d.right:                                                             #如果左節點存在右節點
                    delnode.right = d.right                                      #要刪去的節點的右指針指向左節點的右節點
                    return delnode.right
                delnode.left = None                                     #刪去要刪去節點的左節點(因為左節點已經替換的原要刪去的節點)
            elif delnode.left == None and delnode.right:
                d = delnode.right 
                delnode.val = d.val
                return delnode
                if d.left:
                    delnode.left = d.left
                    return delnode.left
                if d.right:
                    delnode.right = d.right
                    return delnode.right
                delnode.right  = None
            elif delnode.left == None and delnode.right == None:   #如果要刪去節點沒有左右節點，即要刪去節點為葉節點
                delnode = None                                                        #直接刪去要刪去的節點
            else:                                                             #要刪去節點有左右節點
                p = delnode.right 
                parent = None
                while p.left:                                                      #如果要刪去節點的右節點存在左節點，找出最小值
                    parent = p
                    p = p.left
                delnode.val = p.val                                           #把最小值的值複製給要刪除的節點
                #parent.left = None
                if p.right:                                                        #如果最小值存在右節點
                    #q=p.right
                    parent.left = None
                    parent.left = p.right                                            #把刪去節點的父節點指向刪去節點的右節點
                else:
                    parent.left = None
                p = None                                                        #刪除最小節點
                return root
           
            
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution().delete(root1,8)
print(a.val)
#print(a.left.val)
#print(a.left.left.val)
#print(a.left.left.left.val)
#print(a.right.val)
#print(a.right.left.val)
print(a.right.left.left == None)
#print(a.right.right.val)
#print(a.right.val == 8 and a.right.left.val ==7 and a.right.left.left.val ==6)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-20-1f25ce1732ef> in <module>()
          7 root1.right.left = TreeNode(7)
          8 root1.right.left.left = TreeNode(6)
    ----> 9 a = Solution().delete(root1,8)
         10 print(a.val)
         11 #print(a.left.val)


    <ipython-input-19-6133913bd0dd> in delete(self, root, target)
        109                     parent.left = p.right                                            #把刪去節點的父節點指向刪去節點的右節點
        110                 else:
    --> 111                     parent.left = None
        112                 p = None                                                        #刪除最小節點
        113                 return root


    AttributeError: 'NoneType' object has no attribute 'left'



```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if target == root.val:                        #當刪去的節點是根節點時
            if root.right == None and root.left:                      #當根節點只有左節點時
                root = root.left
                return root
            elif root.left == None and root.right:                   #當根節點只有右節點時
                root = root.right
                return root
            elif root.right == None and root.left == None:     #當根節點沒有左右節點，即樹裡只有根節點
                root = None
                return root
            else:                                                              #當根節點左右兩點都有時
                p = root.right                                                      #選擇尋找右子樹的最小值
                while p.left:                                                         #找最小值，直到找到最小值，跳出迴圈
                    parent = p                                                      #記錄父節點的位置
                    p = p.left                                                        #走到下一個左節點
                if p.right:                                                    #如果最小值存在右節點
                    q = p.right
                    parent.left = q                                        #parent指向替換值的右節點
                p.left = root.left  #p是找到的最小值，替換根節點。則p的左指針指向原本根節點的左邊
                p.right = root.right  #p的右指針指向本來的根節點的右邊
                root = None       #刪掉根節點
                return p             #要記得回傳p的值
        else:                                               #當刪去的節點不是根節點時，即target != root.val
            delnode = Solution().search(root,target)            #找到要刪去的節點，記為delnode
            if delnode.right == None and delnode.left:             #當要刪去節點只有左節點時
                d = delnode.left
                delnode.val = d.val                                                #把左節點的值賦給要刪去的節點
                return delnode
                if d.left:                                                               #如果左節點還存在左節點
                    delnode.left = d.left                                          #要刪去的節點的左指針指向左節點的左節點 
                    return delnode.left
                if d.right:                                                             #如果左節點存在右節點
                    delnode.right = d.right                                      #要刪去的節點的右指針指向左節點的右節點
                    return delnode.right
                delnode.left = None                                     #刪去要刪去節點的左節點(因為左節點已經替換的原要刪去的節點)
            elif delnode.left == None and delnode.right:
                d = delnode.right 
                delnode.val = d.val
                return delnode
                if d.left:
                    delnode.left = d.left
                    return delnode.left
                if d.right:
                    delnode.right = d.right
                    return delnode.right
                delnode.right  = None
            elif delnode.left == None and delnode.right == None:   #如果要刪去節點沒有左右節點，即要刪去節點為葉節點
                delnode = None                                                        #直接刪去要刪去的節點
            else:                                                             #要刪去節點有左右節點
                p = delnode.right                                   
                while p.left:                                                      #如果要刪去節點的右節點存在左節點，找出最小值
                    parent = p
                    p = p.left                                                     #p即為最小值節點
                delnode.val = p.val                                           #把最小值的值複製給要刪除的節點
                if p.right:                                                        #如果最小值存在右節點
                    q=p.right                                                    
                    parent.left = q                                             #把刪去節點的父節點指向刪去節點的右節點
                p.left = delnode.left #刪除最小節點
                p.right = delnode.right 
                p = None
                return root
           
            
```

測試如果最小值存在右節點的狀況


```
root1 = TreeNode(8)
root1.left = TreeNode(3)
root1.left.left = TreeNode(2)
root1.left.left.left = TreeNode(2)
root1.left.left.left.left = TreeNode(1)
root1.left.right = TreeNode(4)
root1.left.right.right = TreeNode(5)
root1.right = TreeNode(27)
root1.right.right = TreeNode(38)
root1.right.right.right = TreeNode(49)
root1.right.left = TreeNode(10)
root1.right.left.left = TreeNode(13)
root1.right.left.right = TreeNode(15)
root1.right.right.left = TreeNode(29)
root1.right.right.left.left = TreeNode(26)
root1.right.right.left.right = TreeNode(35)
root1.right.right.left.left.right=TreeNode(28)
a = Solution().delete(root1,27)
print(a.val)
print(a.left.val)
print(a.left.left.val)
print(a.left.left.left.val)
print(a.left.left.left.left.val)
print(a.left.right.val)
print(a.left.right.right.val)
print(a.right.val)
print(a.right.right.val)
print(a.right.right.right.val)
print(a.right.right.left.val)
print(a.right.right.left.left.val)
print(a.right.right.left.right.val)
print(a.right.left.val)
#print(a.right.val)
#print(a.right.left.val)
#print(a.right.left.left.val)
#print(a.right.right.val)
#print(a.right.val == 8 and a.right.left.val ==7 and a.right.left.left.val ==6)
```

    8
    3
    2
    2
    1
    4
    5
    26
    38
    49
    29
    28
    35
    10



```
不存在右節點的狀況，會沒有把它刪掉
```


```
root1 = TreeNode(8)
root1.left = TreeNode(3)
root1.left.left = TreeNode(2)
root1.left.left.left = TreeNode(2)
root1.left.left.left.left = TreeNode(1)
root1.left.right = TreeNode(4)
root1.left.right.right = TreeNode(5)
root1.right = TreeNode(27)
root1.right.right = TreeNode(38)
root1.right.right.right = TreeNode(49)
root1.right.left = TreeNode(10)
root1.right.left.left = TreeNode(13)
root1.right.left.right = TreeNode(15)
root1.right.right.left = TreeNode(29)
root1.right.right.left.left = TreeNode(26)
root1.right.right.left.right = TreeNode(35)
#root1.right.right.left.left.right=TreeNode(28)
a = Solution().delete(root1,27)
print(a.val)
print(a.left.val)
print(a.left.left.val)
print(a.left.left.left.val)
print(a.left.left.left.left.val) #1
print(a.left.right.val)
print(a.left.right.right.val) #5
print(a.right.val)#26
print(a.right.right.val)
print(a.right.right.right.val)
print(a.right.right.left.val)
print(a.right.right.left.left.val)
print(a.right.right.left.right.val)
print(a.right.left.val)
```

    8
    3
    2
    2
    1
    4
    5
    26
    38
    49
    29
    26
    35
    10



```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if Solution().search(root,target) != None:
            if target == root.val:                        #當刪去的節點是根節點時
                if root.right == None and root.left:                      #當根節點只有左節點時
                    root = root.left
                    return root
                elif root.left == None and root.right:                   #當根節點只有右節點時
                    root = root.right
                    return root
                elif root.right == None and root.left == None:     #當根節點沒有左右節點，即樹裡只有根節點
                    root = None
                    return root
                else:                                                               #當根節點左右兩點都有時
                    p = root.right                                                      #選擇尋找右子樹的最小值
                    while p.left:                                                         #找最小值，直到找到最小值，跳出迴圈
                        global parent
                        parent = p                                                      #記錄父節點的位置
                        p = p.left                                                        #走到下一個左節點
                    if p.right:                                                    #如果最小值存在右節點
                        q = p.right
                        parent.left = q                                        #parent指向替換值的右節點
                    else:
                        parent.left = None
                    p.left = root.left  #p是找到的最小值，替換根節點。則p的左指針指向原本根節點的左邊
                    p.right = root.right  #p的右指針指向本來的根節點的右邊
                    root = None       #刪掉根節點
                    return p             #要記得回傳p的值
            else:     #當刪去的節點不是根節點時，即target != root.val
                delnode = Solution().search(root,target)            #找到要刪去的節點，記為delnode
                if delnode.right == None and delnode.left:             #當要刪去節點只有左節點時
                    d = delnode.left
                    delnode.val = d.val                                                #把左節點的值賦給要刪去的節點
                    return delnode
                    if d.left:                                                               #如果左節點還存在左節點
                        delnode.left = d.left                                          #要刪去的節點的左指針指向左節點的左節點 
                        return delnode.left
                    if d.right:                                                             #如果左節點存在右節點
                        delnode.right = d.right                                      #要刪去的節點的右指針指向左節點的右節點
                        return delnode.right
                    delnode.left = None                                     #刪去要刪去節點的左節點(因為左節點已經替換的原要刪去的節點)
                elif delnode.left == None and delnode.right:
                    d = delnode.right 
                    delnode.val = d.val
                    return delnode
                    if d.left:
                        delnode.left = d.left
                        return delnode.left
                    if d.right:
                        delnode.right = d.right
                        return delnode.right
                    delnode.right  = None
                elif delnode.left == None and delnode.right == None:   #如果要刪去節點沒有左右節點，即要刪去節點為葉節點
                    delnode = None #直接刪去要刪去的節點
                else:  #要刪去節點有左右節點
                    p = delnode.right #如果要刪去節點的右節點存在左節點，找出最小值
                    while p.left:
                        parent = p
                        p = p.left  #p即為最小值節點
                    delnode.val = p.val                                           #把最小值的值複製給要刪除的節點
                    if p.right:                                                        #如果最小值存在右節點
                        q=p.right
                        parent.left = q                                             #把刪去節點的父節點指向刪去節點的右節點
                    else:
                        parent.left = None
                    p.left = delnode.left #刪除最小節點
                    p.right = delnode.right 
                    p = None
                    return root
        
                        
                        
```


```
root1 = TreeNode(8)
root1.left = TreeNode(3)
root1.left.left = TreeNode(2)
root1.left.left.left = TreeNode(2)
root1.left.left.left.left = TreeNode(1)
root1.left.right = TreeNode(4)
root1.left.right.right = TreeNode(5)
root1.right = TreeNode(27)
root1.right.right = TreeNode(38)
root1.right.right.right = TreeNode(49)
root1.right.left = TreeNode(10)
root1.right.left.left = TreeNode(13)
root1.right.left.right = TreeNode(15)
root1.right.right.left = TreeNode(29)
root1.right.right.left.left = TreeNode(26)
root1.right.right.left.right = TreeNode(35)
#root1.right.right.left.left.right=TreeNode(28)
a = Solution().delete(root1,49)
print(a.val)
print(a.left.val)
print(a.left.left.val)
print(a.left.left.left.val)
print(a.left.left.left.left.val) #1
print(a.left.right.val)
print(a.left.right.right.val) #5
print(a.right.val)#26
print(a.right.right.val)
print(a.right.right.right==None)
print(a.right.right.left.val)
print(a.right.right.left.left.val)
print(a.right.right.left.right.val)
print(a.right.left.val)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-30-8459f1327e41> in <module>()
         17 #root1.right.right.left.left.right=TreeNode(28)
         18 a = Solution().delete(root1,49)
    ---> 19 print(a.val)
         20 print(a.left.val)
         21 print(a.left.left.val)


    AttributeError: 'NoneType' object has no attribute 'val'



```
root1 = TreeNode(8)
root1.left = TreeNode(3)
root1.left.left = TreeNode(2)
root1.left.left.left = TreeNode(2)
root1.left.left.left.left = TreeNode(1)
root1.left.right = TreeNode(4)
root1.left.right.right = TreeNode(5)
root1.right = TreeNode(27)
root1.right.right = TreeNode(38)
root1.right.right.right = TreeNode(49)
root1.right.left = TreeNode(10)
root1.right.left.left = TreeNode(13)
root1.right.left.right = TreeNode(15)
root1.right.right.left = TreeNode(29)
root1.right.right.left.left = TreeNode(26)
root1.right.right.left.right = TreeNode(35)
#root1.right.right.left.left.right=TreeNode(28)
a = Solution().delete(root1,27)
print(a.val)
print(a.left.val)
print(a.left.left.val)
print(a.left.left.left.val)
print(a.left.left.left.left.val) #1
print(a.left.right.val)
print(a.left.right.right.val) #5
print(a.right.val)#26
print(a.right.right.val)
print(a.right.right.right.val)
print(a.right.right.left.val)
print(a.right.right.left.left==None)
print(a.right.right.left.right.val)
print(a.right.left.val)
```

    8
    3
    2
    2
    1
    4
    5
    26
    38
    49
    29
    True
    35
    10



```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution().delete(root1,5)
print(a.val)
print(a.left.val)
print(a.left.left.val)
print(a.left.left.left.val)
print(a.right.val)
print(a.right.left.val)
print(a.right.left.left==None)
print(a.right.right.val)
#print(a.right.val == 8 and a.right.left.val ==7 and a.right.left.left.val ==6)
```

    6
    3
    3
    -5
    8
    7
    True
    10



```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution().delete(root1,2)
print(a.val)
print(a.left.val)
print(a.left.left.val)
print(a.left.left.left.val)
print(a.right.val)
print(a.right.left.val)
print(a.right.left.left==None)
print(a.right.right.val)
#print(a.right.val == 8 and a.right.left.val ==7 and a.right.left.left.val ==6)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-48-53e7c2466239> in <module>()
          8 root1.right.left.left = TreeNode(6)
          9 a = Solution().delete(root1,2)
    ---> 10 print(a.val)
         11 print(a.left.val)
         12 print(a.left.left.val)


    AttributeError: 'NoneType' object has no attribute 'val'


重複狀況的修改


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    def preorder(self,root,arr):
        if root == None:
            return arr
        else:
            arr.append(root.val)
            if root.left is not None:
                Solution().preorder(root.left,arr)
            if root.right is not None:
                Solution().preorder(root.right,arr)
            return arr
    
    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        arr=[]
        arr=self.preorder(root,arr)
        x=0
        for i in range(len(arr)):
            if arr[i]==target:
                x+=1
        

        while x > 0:
            if target == root.val:                        #當刪去的節點是根節點時
                if root.right == None and root.left:                      #當根節點只有左節點時
                    root = root.left
                    return root
                elif root.left == None and root.right:                   #當根節點只有右節點時
                    root = root.right
                    return root
                elif root.right == None and root.left == None:     #當根節點沒有左右節點，即樹裡只有根節點
                    root = None
                    return root
                else:                                                              #當根節點左右兩點都有時
                    p = root.right                                                      #選擇尋找右子樹的最小值
                    while p.left:                                                         #找最小值，直到找到最小值，跳出迴圈
                        global parent
                        parent = p                                                      #記錄父節點的位置
                        p = p.left                                                        #走到下一個左節點
                    if p.right:                                                    #如果最小值存在右節點
                        q = p.right
                        parent.left = q                                        #parent指向替換值的右節點
                    p.left = root.left  #p是找到的最小值，替換根節點。則p的左指針指向原本根節點的左邊
                    p.right = root.right  #p的右指針指向本來的根節點的右邊
                    root = None       #刪掉根節點
                    return p             #要記得回傳p的值
            else:                                               #當刪去的節點不是根節點時，即target != root.val
                delnode = Solution().search(root,target)            #找到要刪去的節點，記為delnode
                if delnode.right == None and delnode.left:             #當要刪去節點只有左節點時
                    d = delnode.left
                    delnode.val = d.val                                                #把左節點的值賦給要刪去的節點
                    return delnode
                    if d.left:                                                               #如果左節點還存在左節點
                        delnode.left = d.left                                          #要刪去的節點的左指針指向左節點的左節點 
                        return delnode.left
                    if d.right:                                                             #如果左節點存在右節點
                        delnode.right = d.right                                      #要刪去的節點的右指針指向左節點的右節點
                        return delnode.right
                    delnode.left = None                                     #刪去要刪去節點的左節點(因為左節點已經替換的原要刪去的節點)
                elif delnode.left == None and delnode.right:
                    d = delnode.right 
                    delnode.val = d.val
                    return delnode
                    if d.left:
                        delnode.left = d.left
                        return delnode.left
                    if d.right:
                        delnode.right = d.right
                        return delnode.right
                    delnode.right  = None
                elif delnode.left == None and delnode.right == None:   #如果要刪去節點沒有左右節點，即要刪去節點為葉節點
                    delnode = None                                                        #直接刪去要刪去的節點
                else:                                                             #要刪去節點有左右節點
                    p = delnode.right                                   
                    while p.left:                                                      #如果要刪去節點的右節點存在左節點，找出最小值
                        parent = p
                        p = p.left
                    delnode.val = p.val                                           #把最小值的值複製給要刪除的節點
                    if p.right:                                                        #如果最小值存在右節點
                        q=p.right                                                    
                        parent.left = q                                             #把刪去節點的父節點指向刪去節點的右節點
                    p.left = delnode.left #刪除最小節點
                    p.right = delnode.right 
                    p = None
                    return root
                
            i -= 1            
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution().delete(root1,3)
print(a)
#print(a.left.val)
#print(a.left.left.val)
#print(a.left.left.left.val)
#print(a.right.val)
#print(a.right.left.val)
#print(a.right.left.left==None)
#print(a.right.right.val)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-19-2d3290a1d991> in <module>()
          7 root1.right.left = TreeNode(7)
          8 root1.right.left.left = TreeNode(6)
    ----> 9 a = Solution().delete(root1,3)
         10 print(a)
         11 #print(a.left.val)


    <ipython-input-17-54a781d8783c> in delete(self, root, target)
         72             else:                                               #當刪去的節點不是根節點時，即target != root.val
         73                 delnode = Solution().search(root,target)            #找到要刪去的節點，記為delnode
    ---> 74                 if delnode.right == None and delnode.left:             #當要刪去節點只有左節點時
         75                     d = delnode.left
         76                     delnode.val = d.val                                                #把左節點的值賦給要刪去的節點


    AttributeError: 'NoneType' object has no attribute 'right'



```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        
        while Solution().search(root,target) != None:
            
            if target == root.val:                        #當刪去的節點是根節點時
                if root.right == None and root.left:                      #當根節點只有左節點時
                    root = root.left
                    return root
                elif root.left == None and root.right:                   #當根節點只有右節點時
                    root = root.right
                    return root
                elif root.right == None and root.left == None:     #當根節點沒有左右節點，即樹裡只有根節點
                    root = None
                    return root
                else:                                                              #當根節點左右兩點都有時
                    p = root.right                                                      #選擇尋找右子樹的最小值
                    while p.left:                                                         #找最小值，直到找到最小值，跳出迴圈
                        global parent
                        parent = p                                                      #記錄父節點的位置
                        p = p.left                                                        #走到下一個左節點
                    if p.right:                                                    #如果最小值存在右節點
                        q = p.right
                        parent.left = q                                        #parent指向替換值的右節點
                    p.left = root.left  #p是找到的最小值，替換根節點。則p的左指針指向原本根節點的左邊
                    p.right = root.right  #p的右指針指向本來的根節點的右邊
                    root = None       #刪掉根節點
                    return p             #要記得回傳p的值
            else:                                               #當刪去的節點不是根節點時，即target != root.val
                delnode = Solution().search(root,target)            #找到要刪去的節點，記為delnode
                if delnode.right == None and delnode.left:             #當要刪去節點只有左節點時
                    d = delnode.left
                    delnode.val = d.val                                                #把左節點的值賦給要刪去的節點
                    return delnode
                    if d.left:                                                               #如果左節點還存在左節點
                        delnode.left = d.left                                          #要刪去的節點的左指針指向左節點的左節點 
                        return delnode.left
                    if d.right:                                                             #如果左節點存在右節點
                        delnode.right = d.right                                      #要刪去的節點的右指針指向左節點的右節點
                        return delnode.right
                    delnode.left = None                                     #刪去要刪去節點的左節點(因為左節點已經替換的原要刪去的節點)
                elif delnode.left == None and delnode.right:
                    d = delnode.right 
                    delnode.val = d.val
                    return delnode
                    if d.left:
                        delnode.left = d.left
                        return delnode.left
                    if d.right:
                        delnode.right = d.right
                        return delnode.right
                    delnode.right  = None
                elif delnode.left == None and delnode.right == None:   #如果要刪去節點沒有左右節點，即要刪去節點為葉節點
                    delnode = None                                                        #直接刪去要刪去的節點
                else:                                                             #要刪去節點有左右節點
                    p = delnode.right                                   
                    while p.left:                                                      #如果要刪去節點的右節點存在左節點，找出最小值
                        parent = p
                        p = p.left
                    delnode.val = p.val                                           #把最小值的值複製給要刪除的節點
                    if p.right:                                                        #如果最小值存在右節點
                        q=p.right                                                    
                        parent.left = q                                             #把刪去節點的父節點指向刪去節點的右節點
                    p.left = delnode.left #刪除最小節點
                    p.right = delnode.right 
                    p = None
                    return root                  
        
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution().delete(root1,3)
print(a.val)
print(a.left.val)
print(a.left.left.val)
print(a.left.left.left.val)
#print(a.right.val)
#print(a.right.left.val)
#print(a.right.left.left.val)
#print(a.right.right.val)

```

    3
    3
    -5



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-47-c99808360a2c> in <module>()
         11 print(a.left.val)
         12 print(a.left.left.val)
    ---> 13 print(a.left.left.left.val)
         14 #print(a.right.val)
         15 #print(a.right.left.val)


    AttributeError: 'NoneType' object has no attribute 'val'



```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        a = Solution().search(root,target)
        if a == None:
            if target == root.val:                        #當刪去的節點是根節點時
                if root.right == None and root.left:                      #當根節點只有左節點時
                    root = root.left
                    return root
                elif root.left == None and root.right:                   #當根節點只有右節點時
                    root = root.right
                    return root
                elif root.right == None and root.left == None:     #當根節點沒有左右節點，即樹裡只有根節點
                    root = None
                    return root
                else:                                                               #當根節點左右兩點都有時
                    p = root.right                                                      #選擇尋找右子樹的最小值
                    while p.left:                                                         #找最小值，直到找到最小值，跳出迴圈
                        global parent
                        parent = p                                                      #記錄父節點的位置
                        p = p.left                                                        #走到下一個左節點
                    if p.right:                                                    #如果最小值存在右節點
                        q = p.right
                        parent.left = q                                        #parent指向替換值的右節點
                    else:
                        parent.left = None
                    p.left = root.left  #p是找到的最小值，替換根節點。則p的左指針指向原本根節點的左邊
                    p.right = root.right  #p的右指針指向本來的根節點的右邊
                    root = None       #刪掉根節點
                    return p             #要記得回傳p的值
            else:     #當刪去的節點不是根節點時，即target != root.val
                delnode = Solution().search(root,target)            #找到要刪去的節點，記為delnode
                if delnode.right == None and delnode.left:             #當要刪去節點只有左節點時
                    d = delnode.left
                    delnode.val = d.val                                                #把左節點的值賦給要刪去的節點
                    return delnode
                    if d.left:                                                               #如果左節點還存在左節點
                        delnode.left = d.left                                          #要刪去的節點的左指針指向左節點的左節點 
                        return delnode.left
                    if d.right:                                                             #如果左節點存在右節點
                        delnode.right = d.right                                      #要刪去的節點的右指針指向左節點的右節點
                        return delnode.right
                    delnode.left = None                                     #刪去要刪去節點的左節點(因為左節點已經替換的原要刪去的節點)
                elif delnode.left == None and delnode.right:
                    d = delnode.right 
                    delnode.val = d.val
                    return delnode
                    if d.left:
                        delnode.left = d.left
                        return delnode.left
                    if d.right:
                        delnode.right = d.right
                        return delnode.right
                    delnode.right  = None
                elif delnode.left == None and delnode.right == None:   #如果要刪去節點沒有左右節點，即要刪去節點為葉節點
                    delnode = None #直接刪去要刪去的節點
                else:  #要刪去節點有左右節點
                    p = delnode.right #如果要刪去節點的右節點存在左節點，找出最小值
                    while p.left:
                        parent = p
                        p = p.left  #p即為最小值節點
                    delnode.val = p.val                                           #把最小值的值複製給要刪除的節點
                    if p.right:                                                        #如果最小值存在右節點
                        q=p.right
                        parent.left = q                                             #把刪去節點的父節點指向刪去節點的右節點
                    else:
                        parent.left = None
                    p.left = delnode.left #刪除最小節點
                    p.right = delnode.right 
                    p = None
                    return root
        else:
            return root
        
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution().delete(root1,2)
print(a.val)
print(a.left.val)
print(a.left.left.val)
print(a.left.left.left.val)
print(a.right.val)
print(a.right.left.val)
print(a.right.left.left.val)
print(a.right.right.val)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-57-508db29837df> in <module>()
          7 root1.right.left = TreeNode(7)
          8 root1.right.left.left = TreeNode(6)
    ----> 9 a = Solution().delete(root1,2)
         10 print(a.val)
         11 print(a.left.val)


    <ipython-input-56-86ea24177373> in delete(self, root, target)
         70             else:     #當刪去的節點不是根節點時，即target != root.val
         71                 delnode = Solution().search(root,target)            #找到要刪去的節點，記為delnode
    ---> 72                 if delnode.right == None and delnode.left:             #當要刪去節點只有左節點時
         73                     d = delnode.left
         74                     delnode.val = d.val                                                #把左節點的值賦給要刪去的節點


    AttributeError: 'NoneType' object has no attribute 'right'



```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
        
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution()
print(a.search(root1,2)==None)
#print(a.left.left.val)
#print(a.left.left.left.val)
#print(a.right.val)
#print(a.right.left.val)
#print(a.right.left.left.val)
#print(a.right.right.val)
```

    True



```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution()
print(a.search(root1,6)==root1.right.left.left)

class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
        
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
print(Solution().search(root1,2))
```

    None


又考慮到如果要刪除的值不在BST裡面，就直接pass不改變原有的測資料


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        a = Solution().search(root,target)
        if a != None:
            if target == root.val:                        #當刪去的節點是根節點時
                if root.right == None and root.left:                      #當根節點只有左節點時
                    root = root.left
                    return root
                elif root.left == None and root.right:                   #當根節點只有右節點時
                    root = root.right
                    return root
                elif root.right == None and root.left == None:     #當根節點沒有左右節點，即樹裡只有根節點
                    root = None
                    return root
                else:                                                               #當根節點左右兩點都有時
                    p = root.right                                                      #選擇尋找右子樹的最小值
                    while p.left:                                                         #找最小值，直到找到最小值，跳出迴圈
                        global parent
                        parent = p                                                      #記錄父節點的位置
                        p = p.left                                                        #走到下一個左節點
                    if p.right:                                                    #如果最小值存在右節點
                        q = p.right
                        parent.left = q                                        #parent指向替換值的右節點
                    else:
                        parent.left = None
                    p.left = root.left  #p是找到的最小值，替換根節點。則p的左指針指向原本根節點的左邊
                    p.right = root.right  #p的右指針指向本來的根節點的右邊
                    root = None       #刪掉根節點
                    return p             #要記得回傳p的值
            else:     #當刪去的節點不是根節點時，即target != root.val
                delnode = Solution().search(root,target)            #找到要刪去的節點，記為delnode
                if delnode.right == None and delnode.left:             #當要刪去節點只有左節點時
                    d = delnode.left
                    delnode.val = d.val                                                #把左節點的值賦給要刪去的節點
                    return delnode
                    if d.left:                                                               #如果左節點還存在左節點
                        delnode.left = d.left                                          #要刪去的節點的左指針指向左節點的左節點 
                        return delnode.left
                    if d.right:                                                             #如果左節點存在右節點
                        delnode.right = d.right                                      #要刪去的節點的右指針指向左節點的右節點
                        return delnode.right
                    delnode.left = None                                     #刪去要刪去節點的左節點(因為左節點已經替換的原要刪去的節點)
                elif delnode.left == None and delnode.right:
                    d = delnode.right 
                    delnode.val = d.val
                    return delnode
                    if d.left:
                        delnode.left = d.left
                        return delnode.left
                    if d.right:
                        delnode.right = d.right
                        return delnode.right
                    delnode.right  = None
                elif delnode.left == None and delnode.right == None:   #如果要刪去節點沒有左右節點，即要刪去節點為葉節點
                    del delnode
                    #delnode = None #直接刪去要刪去的節點
                else:  #要刪去節點有左右節點
                    p = delnode.right #如果要刪去節點的右節點存在左節點，找出最小值
                    while p.left:
                        parent = p
                        p = p.left  #p即為最小值節點
                    delnode.val = p.val                                           #把最小值的值複製給要刪除的節點
                    if p.right:                                                        #如果最小值存在右節點
                        q=p.right
                        parent.left = q                                             #把刪去節點的父節點指向刪去節點的右節點
                    else:
                        parent.left = None
                    p.left = delnode.left #刪除最小節點
                    p.right = delnode.right 
                    p = None
                    return root
        else:
            return root
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
root1.right.right.right = TreeNode(11)
a = Solution().delete(root1,6)
print(a.val)
#print(a.left.val)
#print(a.left.left.val)
#print(a.left.left.left.val)
#print(a.right.val)
#print(a.right.left.val)
#print(a.right.left.left.val)
#print(a.right.right.val)
#print(a.right.right.right.val)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-23-02e328f1580e> in <module>()
          9 root1.right.right.right = TreeNode(11)
         10 a = Solution().delete(root1,6)
    ---> 11 print(a.val)
         12 #print(a.left.val)
         13 #print(a.left.left.val)


    AttributeError: 'NoneType' object has no attribute 'val'


重複值的狀況


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        a = Solution().search(root,target)
        if Solution().search(root,target) != None:
            while Solution().search(root,target) != None:
                if target == root.val:     #情況一：當刪去的節點是根節點時
                    if root.right == None and root.left:                      #情況一(1)：當根節點只有左節點時
                        root = root.left
                        return root
                    elif root.left == None and root.right:                   #情況一(2)：當根節點只有右節點時
                        root = root.right
                        return root
                    elif root.right == None and root.left == None:     #情況一(3)：當根節點沒有左右節點，即樹裡只有根節點
                        root = None
                        return root
                    else:                                                               #情況一(4)：當根節點左右兩點都有時
                        p = root.right                                                      #選擇尋找右子樹的最小值
                        while p.left:                                                         #找最小值，直到找到最小值，跳出迴圈
                            global parent
                            parent = p                                                      #記錄父節點的位置
                            p = p.left                                                        #走到下一個左節點
                        if p.right:                                                    #情況一(4A)：如果最小值存在右節點
                            q = p.right
                            parent.left = q                                        #parent指向替換值的右節點
                        else:                                                         #情況一(4B)：如果最小值不存在右節點
                            parent.left = None
                            
                        p.left = root.left      #p是找到的最小值，替換根節點。則p的左指針指向原本根節點的左邊
                        p.right = root.right  #p的右指針指向本來的根節點的右邊
                        root = None          #刪掉根節點
                        return p               #要記得回傳p的值
                else:                             #情況二：當刪去的節點不是根節點時，即target != root.val
                    delnode = Solution().search(root,target)            #找到要刪去的節點，記為delnode
                    if delnode.right == None and delnode.left:             #情況二(1)：當要刪去節點只有左節點時
                        d = delnode.left
                        delnode.val = d.val                                                #把左節點的值賦給要刪去的節點
                        return delnode
                    
                        if d.left:                                                               #如果左節點還存在左節點
                            delnode.left = d.left                                          #要刪去的節點的左指針指向左節點的左節點 
                            return delnode.left
                        if d.right:                                                             #如果左節點存在右節點
                            delnode.right = d.right                                      #要刪去的節點的右指針指向左節點的右節點
                            return delnode.right
                        delnode.left = None                                     #刪去要刪去節點的左節點(因為左節點已經替換的原要刪去的節點)
                    elif delnode.left == None and delnode.right:       #情況二(2)：當要刪去節點只有右節點時
                        d = delnode.right 
                        delnode.val = d.val
                        return delnode
                        if d.left:
                            delnode.left = d.left
                            return delnode.left
                        if d.right:
                            delnode.right = d.right
                            return delnode.right
                        delnode.right  = None
                    elif delnode.left == None and delnode.right == None:   #情況二(3)：當刪去節點沒有左右節點，即要刪去節點為葉節點
                        delnode = None #直接刪去要刪去的節點
                        return delnode
                        
                    else:                                                                      #情況二(4)：要刪去節點有左右節點
                        if delnode.right.left  and delnode.right.right == None:            #情況二(4A)：要刪去節點的右節點有右節點
                            p = delnode.right
                            while p.left:
                                parent = p
                                p = p.left
                            delnode.val = p.val
                            if p.right:
                                q=p.right
                                parent.left = q
                            else:
                                parent.left = None
                            p.left = delnode.left
                            p.right = delnode.right
                            p = None
                            return p
                        elif delnode.right.left and delnode.right.right:                       #情況二(4B)：要刪去節點的右節點有左節點和右節點
                            p = delnode.right
                            while p.left:
                                parent = p
                                p = p.left
                            delnode.val = p.val
                            if p.right:
                                q=p.right
                                parent.left = q
                            else:
                                parent.left = None
                            p.left = delnode.left
                            p.right = delnode.right
                            p = None
                            return p
                        elif delnode.right.left == None and delnode.right.right == None: #情況二(4C)：要刪去節點的右節點沒有左右節點
                            delnode.val = delnode.right.val
                            delnode.right = None
                            return delnode
                        else:                                                                                   #情況二(4D)：刪去節點的右節點只存在右節點無左節點
                            p = delnode.right
                            delnode.val = p.val
                            p.left = delnode.left
                            p.right = delnode.right.right
                            p = None
                            return root
        else:   #如果刪除值不在BST裡，則直接pass回傳原測資
            return root
                    
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
#Solution().search(root1,11)
a = Solution().delete(root1,3)
#print(Solution().delete(root1,3).val)
print(a.val)
print(a.left.val)
print(a.left.left.val)
print(a.left.left.left.val)
print(a.right.val)
print(a.right.left.val)
#print(a.right.left.left.val)
print(a.right.right.val)
```

    3
    3
    -5



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-37-1316470ba817> in <module>()
         13 print(a.left.val)
         14 print(a.left.left.val)
    ---> 15 print(a.left.left.left.val)
         16 print(a.right.val)
         17 print(a.right.left.val)


    AttributeError: 'NoneType' object has no attribute 'val'



```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        #if Solution().search(root,target) != None:
        if target == root.val:                        #當刪去的節點是根節點時
            if root.right == None and root.left:                      #當根節點只有左節點時
                    root = root.left
                    return root
            elif root.left == None and root.right:                   #當根節點只有右節點時
                    root = root.right
                    return root
            elif root.right == None and root.left == None:     #當根節點沒有左右節點，即樹裡只有根節點
                    root = None
                    return root
                    
            else:                                                               #當根節點左右兩點都有時
                    p = root.right                                                      #選擇尋找右子樹的最小值
                    while p.left:                                                         #找最小值，直到找到最小值，跳出迴圈
                        global parent
                        parent = p                                                      #記錄父節點的位置
                        p = p.left                                                        #走到下一個左節點
                    if p.right:                                                    #如果最小值存在右節點
                        q = p.right
                        parent.left = q                                        #parent指向替換值的右節點
                    else:
                        parent.left = None
                    p.left = root.left  #p是找到的最小值，替換根節點。則p的左指針指向原本根節點的左邊
                    p.right = root.right  #p的右指針指向本來的根節點的右邊
                    root = None       #刪掉根節點
                    return p             #要記得回傳p的值
        else:     #當刪去的節點不是根節點時，即target != root.val
            if target<=root.val:
                    self.delete(root.left,target)
            else:
                    self.delete(root.right,target)
                    
            return root
                #delnode = Solution().search(root,target)            #找到要刪去的節點，記為delnode
                #if delnode.right == None and delnode.left:             #當要刪去節點只有左節點時
                  #  d = delnode.left
                    #delnode.val = d.val                                                #把左節點的值賦給要刪去的節點
                    #return delnode
                    #if d.left:                                                               #如果左節點還存在左節點
                      #  delnode.left = d.left                                          #要刪去的節點的左指針指向左節點的左節點 
                        #return delnode.left
                    #if d.right:                                                             #如果左節點存在右節點
                      #  delnode.right = d.right                                      #要刪去的節點的右指針指向左節點的右節點
                        #return delnode.right
                    #delnode.left = None                                     #刪去要刪去節點的左節點(因為左節點已經替換的原要刪去的節點)
                #elif delnode.left == None and delnode.right:
                  #  d = delnode.right 
                    #delnode.val = d.val
                    #return delnode
                    #if d.left:
                      #  delnode.left = d.left
                        #return delnode.left
                    #if d.right:
                      #  delnode.right = d.right
                        #return delnode.right
                    #delnode.right  = None
                #elif delnode.left == None and delnode.right == None:   #如果要刪去節點沒有左右節點，即要刪去節點為葉節點
                    #delnode = None #直接刪去要刪去的節點
                  #  del delnode
                #else:  #要刪去節點有左右節點
                  #  p = delnode.right #如果要刪去節點的右節點存在左節點，找出最小值
                    #while p.left:
                      #  parent = p
                       # p = p.left  #p即為最小值節點
                    #delnode.val = p.val                                           #把最小值的值複製給要刪除的節點
                    #if p.right:                                                        #如果最小值存在右節點
                      #  q=p.right
                        #parent.left = q                                             #把刪去節點的父節點指向刪去節點的右節點
                    #else:
                      #  parent.left = None
                    #p.left = delnode.left #刪除最小節點
                    #p.right = delnode.right 
                    #p = None
                    #return root
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
#Solution().search(root1,11)
a = Solution().delete(root1,5)
#print(Solution().delete(root1,3).val)
print(a.val)
print(a.left.val)
print(a.left.left.val)
print(a.left.left.left.val)
print(a.right.val)
print(a.right.left.val)
#print(a.right.left.left.val)
print(a.right.right.val)
```

    6
    3
    3
    -5
    8
    7
    10



```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
#Solution().search(root1,11)
a = Solution().delete(root1,2)
#print(Solution().delete(root1,3).val)
print(a.val)
print(a.left.val)
print(a.left.left.val)
print(a.left.left.left.val)
print(a.right.val)
print(a.right.left.val)
#print(a.right.left.left.val)
print(a.right.right.val)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-104-943f6631144d> in <module>()
          8 root1.right.left.left = TreeNode(6)
          9 #Solution().search(root1,11)
    ---> 10 a = Solution().delete(root1,2)
         11 #print(Solution().delete(root1,3).val)
         12 print(a.val)


    <ipython-input-99-f756e4f898ae> in delete(self, root, target)
         69         else:     #當刪去的節點不是根節點時，即target != root.val
         70             if target<=root.val:
    ---> 71                     self.delete(root.left,target)
         72             else:
         73                     self.delete(root.right,target)


    <ipython-input-99-f756e4f898ae> in delete(self, root, target)
         69         else:     #當刪去的節點不是根節點時，即target != root.val
         70             if target<=root.val:
    ---> 71                     self.delete(root.left,target)
         72             else:
         73                     self.delete(root.right,target)


    <ipython-input-99-f756e4f898ae> in delete(self, root, target)
         69         else:     #當刪去的節點不是根節點時，即target != root.val
         70             if target<=root.val:
    ---> 71                     self.delete(root.left,target)
         72             else:
         73                     self.delete(root.right,target)


    <ipython-input-99-f756e4f898ae> in delete(self, root, target)
         71                     self.delete(root.left,target)
         72             else:
    ---> 73                     self.delete(root.right,target)
         74 
         75             return root


    <ipython-input-99-f756e4f898ae> in delete(self, root, target)
         42         """
         43         #if Solution().search(root,target) != None:
    ---> 44         if target == root.val:                        #當刪去的節點是根節點時
         45             if root.right == None and root.left:                      #當根節點只有左節點時
         46                     root = root.left


    AttributeError: 'NoneType' object has no attribute 'val'



```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
#Solution().search(root1,11)
a = Solution().delete(root1,6)
#print(Solution().delete(root1,3).val)
print(a.val)
print(a.left.val)
print(a.left.left.val)
print(a.left.left.left.val)
print(a.right.val)
print(a.right.left.val)
print(a.right.left.left.val)
print(a.right.right.val)
```

    5
    3
    3
    -5
    8
    7
    6
    10



```
root1 = TreeNode(8)
root1.left = TreeNode(3)
root1.left.left = TreeNode(2)
root1.left.left.left = TreeNode(2)
root1.left.left.left.left = TreeNode(1)
root1.left.right = TreeNode(4)
root1.left.right.right = TreeNode(5)
root1.right = TreeNode(27)
root1.right.right = TreeNode(38)
root1.right.right.right = TreeNode(49)
root1.right.left = TreeNode(10)
root1.right.left.left = TreeNode(13)
root1.right.left.right = TreeNode(15)
root1.right.right.left = TreeNode(29)
root1.right.right.left.left = TreeNode(26)
root1.right.right.left.right = TreeNode(35)
#root1.right.right.left.left.right=TreeNode(28)
a = Solution().delete(root1,35)
print(a.val)
print(a.left.val)
print(a.left.left.val)
print(a.left.left.left.val)
print(a.left.left.left.left.val) #1
print(a.left.right.val)
print(a.left.right.right.val) #5
print(a.right.val)#26
print(a.right.right.val)
print(a.right.right.right.val)
print(a.right.right.left.val)
print(a.right.right.left.left.val)
print(a.right.right.left.right.val)
print(a.right.left.val)
```


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    def preorder(self,root,arr):
        if root == None:
            return arr
        else:
            arr.append(root.val)
            if root.left is not None:
                Solution().preorder(root.left,arr)
            if root.right is not None:
                Solution().preorder(root.right,arr)
            return arr
    
    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        arr=[]
        arr=self.preorder(root,arr)
        x=0
        for i in range(len(arr)):
            if arr[i]==target:
                x+=1    
        if x==0:
            return root
        else:
            for i in range(x):
                self.remove(root,target)
            return root
                
    def remove(self,root,target):
                if target == root.val:                        #當刪去的節點是根節點時
                    if root.right == None and root.left:                      #當根節點只有左節點時
                        return root.left
                    elif root.left == None and root.right:                   #當根節點只有右節點時
                        return root.right
                    elif root.right == None and root.left == None:     #當根節點沒有左右節點，即樹裡只有根節點
                        del root
                    else:                                                               #當根節點左右兩點都有時
                        p = root.right                                                      #選擇尋找右子樹的最小值
                        while p.left:                                                         #找最小值，直到找到最小值，跳出迴圈
                            global parent
                            parent = p                                                      #記錄父節點的位置
                            p = p.left                                                        #走到下一個左節點
                        if p.right:                                                    #如果最小值存在右節點
                            q = p.right
                            parent.left = q                                        #parent指向替換值的右節點
                        else:
                            parent.left = None
                        p.left = root.left  #p是找到的最小值，替換根節點。則p的左指針指向原本根節點的左邊
                        p.right = root.right  #p的右指針指向本來的根節點的右邊
                        root = None       #刪掉根節點
                        return p             #要記得回傳p的值
                else:     #當刪去的節點不是根節點時，即target != root.val
                    if target<=root.val:
                        self.remove(root.left,target)
                    else:
                        self.remove(root.right,target)
                
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
#Solution().search(root1,11)
a = Solution().delete(root1,5)
#print(Solution().delete(root1,3).val)
print(a.val)
print(a.left.val)
print(a.left.left.val)
print(a.left.left.left.val)
print(a.right.val)
print(a.right.left.val)
#print(a.right.left.left.val)
print(a.right.right.val)
```

    5
    3
    3
    -5
    8
    7
    10



```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    def preorder(self,root,arr):
        if root == None:
            return arr
        else:
            arr.append(root.val)
            if root.left is not None:
                Solution().preorder(root.left,arr)
            if root.right is not None:
                Solution().preorder(root.right,arr)
            return arr
    
    
    def delete(self, root,target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        array=[]
        array=self.preorder(root , array)
        print(array)
        x=0
        for i in range(len(array)):
            if array[i]==target:
                x+=1    
        print(x)
        
```


```
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.left.left = TreeNode(3)
root1.left.left.left = TreeNode(-5)
root1.right = TreeNode(8)
root1.right.right = TreeNode(10)
root1.right.left = TreeNode(7)
root1.right.left.left = TreeNode(6)
a = Solution().delete(root1,4)
```

    [5, 3, 3, -5, 8, 7, 6, 10]
    0



```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    def preorder(self,root,arr):
        if root == None:
            return arr
        else:
            arr.append(root.val)
            if root.left is not None:
                Solution().preorder(root.left,arr)
            if root.right is not None:
                Solution().preorder(root.right,arr)
            return arr
    
    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        arr=[]
        arr=self.preorder(root,arr)
        x=0
        for i in range(len(arr)):
            if arr[i]==target:
                x+=1    
        if x==0:
            return root
        else:
            for i in range(x):
                self.remove(root,target)
            return root
                
    def remove(self,root,target):
                if target == root.val:                        #當刪去的節點是根節點時
                    if root.right == None and root.left:                      #當根節點只有左節點時
                        return root.left
                    elif root.left == None and root.right:                   #當根節點只有右節點時
                        return root.right
                    elif root.right == None and root.left == None:     #當根節點沒有左右節點，即樹裡只有根節點
                        del root
                    else:                                                               #當根節點左右兩點都有時
                        minnode = Solution().FindMin(root)
                        p = minnode
                        root = minnode
                        minnode.left = root.left
                        minnode.right = root.right
                        p = minnode.right
                        
                        
                        
                        
                        minnode = None
                        
                        
                        
                        
                        
                        
                        p = root.right                                                      #選擇尋找右子樹的最小值
                        while p.left:                                                         #找最小值，直到找到最小值，跳出迴圈
                            global parent
                            parent = p                                                      #記錄父節點的位置
                            p = p.left                                                        #走到下一個左節點
                        if p.right:                                                    #如果最小值存在右節點
                            q = p.right
                            parent.left = q                                        #parent指向替換值的右節點
                        else:
                            parent.left = None
                        p.left = root.left  #p是找到的最小值，替換根節點。則p的左指針指向原本根節點的左邊
                        p.right = root.right  #p的右指針指向本來的根節點的右邊
                        root = None       #刪掉根節點
                        return p             #要記得回傳p的值
                else:     #當刪去的節點不是根節點時，即target != root.val
                    if target<=root.val:
                        self.remove(root.left,target)
                    else:
                        self.remove(root.right,target)
                
```


```
更改了左右節點都存在的狀況
```


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):
        if root.left:
            self.FindMin(root.left)
        else:
            return root
        
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root == None:
            root =TreeNode(val)
            return root
       # if val <= root.val:                          #考慮重複值的insert，把它insert到離root最近的地方
         #   SameNode = TreeNode(val)       #創建重複值的節點
           # SameNode.left = root.left          #重複值的左指針指向原本root的左節點
            #root.left = SameNode               #現在的root的左節點指向重複值節點
            #return   SameNode
        
        elif val<=root.val:
            if root.left:
                return Solution().insert(root.left, val)
            else:
                root.left = TreeNode(val)
                return root
        else:
            if root.right:
                return Solution().insert(root.right,val)
            else:
                root.right = TreeNode(val)
                return root        
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    def preorder(self,root,arr):
        if root == None:
            return arr
        else:
            arr.append(root.val)
            if root.left is not None:
                Solution().preorder(root.left,arr)
            if root.right is not None:
                Solution().preorder(root.right,arr)
            return arr
    
    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        arr=[]
        arr=Solution().preorder(root,arr)
        x=0
        if len(arr)==0:
            print(False)
            return root
        for i in range(len(arr)):
            if arr[i]==target:
                x+=1
                
        if x==0:
            print(False)
            return root
        else:
            for i in range(x-1):
                root=Solution().remove(root,target)
            return root
                
    def remove(self,root,target):
            if target == root.val:                        #當刪去的節點是根節點時
                if root.right == None and root.left:                      #當根節點只有左節點時
                    #return root.left
                    root = root.left
                    return root
                elif root.left == None and root.right:                   #當根節點只有右節點時
                    #return root.right
                    root = root.right
                    return root
                elif root.right == None and root.left == None:     #當根節點沒有左右節點，即樹裡只有根節點
                    del root
                else:                                                               #當根節點左右兩點都有時
                    minnode = Solution().FindMin(root.right)
                    y = minnode.val
                    root = y
                    if minnode.right:
                            z = minnode.right
                            del minnode.right 
                            minnode = z
                    else:
                            del minnode
                
            else:     #當刪去的節點不是根節點時，即target != root.val
                    if target<=root.val:
                        root.left = Solution().remove(root.left,target)
                    else:
                        root.right = Solution().remove(root.right,target)
```


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):
        if root.left is None:
            node1=root.left
            if root.right is None:
                del root
            else:
                root=root.right
            return node1
        else:
            return self.FindMin(root.left)
            
        
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root == None:
            root =TreeNode(val)
            return root
       # if val <= root.val:                          #考慮重複值的insert，把它insert到離root最近的地方
         #   SameNode = TreeNode(val)       #創建重複值的節點
           # SameNode.left = root.left          #重複值的左指針指向原本root的左節點
            #root.left = SameNode               #現在的root的左節點指向重複值節點
            #return   SameNode
        
        elif val<=root.val:
            if root.left:
                return Solution().insert(root.left, val)
            else:
                root.left = TreeNode(val)
                return root
        else:
            if root.right:
                return Solution().insert(root.right,val)
            else:
                root.right = TreeNode(val)
                return root        
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:
            return root
        
        while root.right or root.left:
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    def preorder(self,root,arr):
        if root == None:
            return arr
        else:
            arr.append(root.val)
            if root.left is not None:
                Solution().preorder(root.left,arr)
            if root.right is not None:
                Solution().preorder(root.right,arr)
            return arr
    
    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        arr=[]
        arr=Solution().preorder(root,arr)
        x=0
        if len(arr)==0:
            print(False)
            return root
        for i in range(len(arr)):
            if arr[i]==target:
                x+=1
                
        if x==0:
            print(False)
            return root
        else:
            for i in range(x-1):
                root=self.remove(root,target)
            return root
            
                
    def remove(self,root,target):
            if root == None or (target < root.val and root.left == None) or (target > root.val and root.right == None):
                return False
            elif target == root.val:                        #當刪去的節點是根節點時
                if root.right == None and root.left:                      #當根節點只有左節點時
                    return root.left
                elif root.left == None and root.right:                   #當根節點只有右節點時
                    return root.right
                elif root.right == None and root.left == None:     #當根節點沒有左右節點，即樹裡只有根節點
                    del root
                else:                                                               #當根節點左右兩點都有時
                    minnode = self.FindMin(root.right)
                    root.val=minnode
                     
            else:     #當刪去的節點不是根節點時，即target != root.val
                    if target<=root.val:
                        root.left = self.remove(root.left,target)
                    else:
                        root.right = self.remove(root.right,target)
                    return root
                        


```


```
node1 = TreeNode(5)
Solution().insert(node1,3)
Solution().insert(node1,3)
Solution().insert(node1,-5)
Solution().insert(node1,3)
Solution().insert(node1,8)
#Solution().insert(node1,7)
#Solution().insert(node1,10)
#Solution().insert(node1,6)


Solution().remove(node1,5)
#a = Solution().
arr=[]
Solution().preorder(node1,arr)
arr
```




    [None, 3, 3, -5, 3, 8]



最後增加了modify的狀況


```
class TreeNode(object):
    def __init__(self,x):
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
        self.val = x               #設定當前值為x
        self.left = None        #初始當前值左右沒有節點
        self.right = None

class Solution(object):
    
    def FindMin(self,root):        #設定一個查找最小值的function
        if root.left:
            return Solution().FindMin(root.left)
        else:
            return root
        
    def preorder(self,root,arr):    #設定一個可以遍歷的function
        if root == None:
            return arr
        else:
            arr.append(root.val) #如果root存在，把值append到array裡面
            if root.left != None:    #如果左節點存在，recursive
                Solution().preorder(root.left,arr)
            if root.right != None:  #如果右節點存在，recursive
                Solution().preorder(root.right,arr)
            return arr        
        
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root == None:
            root =TreeNode(val)
            return root
       # if val <= root.val:                          #考慮重複值的insert，把它insert到離root最近的地方
         #   SameNode = TreeNode(val)       #創建重複值的節點
           # SameNode.left = root.left          #重複值的左指針指向原本root的左節點
            #root.left = SameNode               #現在的root的左節點指向重複值節點
            #return   SameNode
        
        elif val<=root.val:
            if root.left:
                return Solution().insert(root.left, val)
            else:
                root.left = TreeNode(val)
                return root
        else:
            if root.right:
                return Solution().insert(root.right,val)
            else:
                root.right = TreeNode(val)
                return root        
         
 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target == root.val:            
            return root
        
        while root.right or root.left:                             #如果左節點不存在或者右節點不存在
            if target > root.val:
                return Solution().search(root.right,target)
            else:
                return Solution().search(root.left,target)
        return None
    
    
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if Solution().search(root,target) != None:
            if target == root.val:                        #當刪去的節點是根節點時
                if root.right == None and root.left:                      #當根節點只有左節點時
                    root = root.left
                    return root
                elif root.left == None and root.right:                   #當根節點只有右節點時
                    root = root.right
                    return root
                elif root.right == None and root.left == None:     #當根節點沒有左右節點，即樹裡只有根節點
                    root = None
                    return root
                    
                else:                                                               #當根節點左右兩點都有時
                    minnode = self.FindMin(root.right)       
                    y = minnode.val
                    root = y
                    if minnode.right:
                            z = minnode.right
                            del minnode.right 
                            minnode = z
                    else:
                            del minnode
                            
            else:     #當刪去的節點不是根節點時，即target != root.val
                if target<=root.val:
                    self.delete(root.left,target)
                else:
                    self.delete(root.right,target)
                    
                return root
        else:
            return root
        
    def modify(self,root,target,new_val):
        if target != new_val:       
            self.insert(root,new_val)
            return Solution().delete(root,target)
        else:
            return root
```


```
node1 = TreeNode(5)
Solution().insert(node1,3)
Solution().insert(node1,3)
Solution().insert(node1,-5)
Solution().insert(node1,3)
Solution().insert(node1,8)
Solution().insert(node1,7)
Solution().insert(node1,10)
Solution().insert(node1,6)


Solution().modify(node1,3,4)
#a = Solution().
arr=[]
Solution().preorder(node1,arr)
arr
```




    [5, 3, 3, -5, 3, 4, 8, 7, 6, 10]




```

```
