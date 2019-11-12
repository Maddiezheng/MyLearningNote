
方法：

divide：不斷的把array從中點分成兩半，一直分一直分一直分一直分一直分直到不能再分

merge：兩兩array比較值的大小，小的在前大的在後，然後一直合一直合一直合一直合一直合直到不能再合

一開始想設定一個空的array，然後使用append的方式把比較大小後的值append進array裡面，但是這樣子就會佔用到外部空間。於是我想到如果直接把比較大小後的值強行更換到原來的array相對應的index裡，這樣就直接使用了原本array的空間。

參考資料：


https://blog.csdn.net/xcq007/article/details/82114657

https://medium.com/appworks-school/初學者學演算法-排序法進階-合併排序法-6252651c6f7e

https://blog.csdn.net/ying_ying_123/article/details/88010540

流程圖：
![jupyter](mergesort流程圖.png)

第一次跑的時候發現if j == None和if I == None的邏輯有點錯誤


```python
class Solution():
    def merge_sort(self,arr):
        mid = len(arr)//2  #這裡的//是省略小數，方便取中點
        left_arr = arr[0:mid]    #左半邊的array
        right_arr = arr[mid:]    #右半邊的array
        Solution().merge_sort(left_arr)      #重複呼叫merge_sort，直到不能再分為止
        Solution().merge_sort(right_arr)
        
        i = 0  #left array的index
        j = 0  #right array的index
        m = 0 #array的index
        while i < len(left_arr) and j < len(right_arr):    #當左右兩個array的index在正確範圍的時候
            if left_arr[i] < right_arr[j]: #比較左右array的指定index大小(從頭開始比較)
                arr[m] = left_arr[i] #若左邊array的值比右邊array大，則把比較後的值更換到最初始array的對應index的值
                i += 1                  #index加一，進行下一個值的比較
                m += 1                #index加一，記錄下一個即將被更換的位置。
            else:
                arr[m] = right_arr[j]
                j += 1
                m += 1
        if j == None:            #此處要考慮當j或i跑到index外面的時候，剩下一邊的array(左或右)的最後一個值直接更換到原array的最後一個位置裡
            arr[m] = left_arr[i]
        
        if I == None:
            arr[m] = right_arr[j
```


      File "<ipython-input-7-36af70fe0147>", line 25
        arr[m] = right_arr[j
                            ^
    SyntaxError: unexpected EOF while parsing



第二次在if裡增加了while迴圈，如果j的index跑出了範圍，此時左邊的array的值可以直接放到原array裡對應的index裡


```python
class Solution():
    def merge_sort(self,arr):
        mid = len(arr)//2  #這裡的//是省略小數，方便取中點
        left_arr = arr[0:mid]    #左半邊的array
        right_arr = arr[mid:]    #右半邊的array
        Solution().merge_sort(left_arr)      #重複呼叫merge_sort，直到array不能再分為止
        Solution().merge_sort(right_arr)
        
        i = 0  #left array的index
        j = 0  #right array的index
        m = 0 #array的index
        while i < len(left_arr) and j < len(right_arr):    #當左右兩個array的index在正確範圍的時候
            if left_arr[i] < right_arr[j]: #比較左右array的指定index大小(從頭開始比較)
                arr[m] = left_arr[i] #若左邊array的值比右邊array大，則把比較後的值更換到最初始array的對應index的值
                i += 1                  #index加一，進行下一個值的比較
                m += 1                #index加一，記錄下一個即將被更換的位置。
            else:
                arr[m] = right_arr[j]
                j += 1
                m += 1
                
        
        if j == None:            #此處要考慮當j或i跑到index外面的時候，剩下一邊的array(左或右)的最後一個值直接更換到原array的最後一個位置裡
            while i < len(left_arr):
                arr[m] = left_arr[i]
                i +=1
                m +=1
            
        if i == None:
            while j <len(right_arr):
                arr[m] = right_arr[j]
                j += 1
                m += 1
        
        
        
```


```python
arr=[10,3,6,5,14,8]
Solution().merge_sort(arr)
```


    ---------------------------------------------------------------------------

    RecursionError                            Traceback (most recent call last)

    <ipython-input-9-90ace2e58113> in <module>()
          1 arr=[10,3,6,5,14,8]
    ----> 2 Solution().merge_sort(arr)
    

    <ipython-input-8-b752ad74a234> in merge_sort(self, arr)
          4         left_arr = arr[0:mid]    #左半邊的array
          5         right_arr = arr[mid:]    #右半邊的array
    ----> 6         Solution().merge_sort(left_arr)      #重複呼叫merge_sort，直到不能再分為止
          7         Solution().merge_sort(right_arr)
          8 


    ... last 1 frames repeated, from the frame below ...


    <ipython-input-8-b752ad74a234> in merge_sort(self, arr)
          4         left_arr = arr[0:mid]    #左半邊的array
          5         right_arr = arr[mid:]    #右半邊的array
    ----> 6         Solution().merge_sort(left_arr)      #重複呼叫merge_sort，直到不能再分為止
          7         Solution().merge_sort(right_arr)
          8 


    RecursionError: maximum recursion depth exceeded while calling a Python object


發現自己忘記考慮如果長度不滿足大於一時的狀況。
並且更改完運行的時候，測試的cell一直在跑，結果一直跑不出來。感覺起來是迴圈的問題，而且code怪怪的，可能要增加別的function


```python
class Solution():
    def merge_sort(self,arr):
         if len(arr) ==1:
            return arr
        
         while len(arr) >1:
            mid = len(arr)//2  #這裡的//是省略小數，方便取中點
            left_arr = arr[0:mid]    #左半邊的array
            right_arr = arr[mid:]    #右半邊的array
            Solution().merge_sort(left_arr)      #重複呼叫merge_sort，直到array不能再分為止
            Solution().merge_sort(right_arr)
            
            i = 0  #left array的index
            j = 0  #right array的index
            m = 0 #array的index
            while i < len(left_arr) and j < len(right_arr):    #當左右兩個array的index在正確範圍的時候
                if left_arr[i] < right_arr[j]: #比較左右array的指定index大小(從頭開始比較)
                    arr[m] = left_arr[i] #若左邊array的值比右邊array大，則把比較後的值更換到最初始array的對應index的值
                    i += 1                  #index加一，進行下一個值的比較
                    m += 1                #index加一，記錄下一個即將被更換的位置。
                else:
                    arr[m] = right_arr[j]
                    j += 1
                    m += 1
            
            if j == None:            #此處要考慮當j或i跑到index外面的時候，剩下一邊的array(左或右)的最後一個值直接更換到原array的最後一個位置裡
                while i < len(left_arr):
                    arr[m] = left_arr[i]
                    i +=1
                    m +=1
            
            if i == None:
                while j <len(right_arr):
                    arr[m] = right_arr[j]
                    j += 1
                    m += 1
```


```python
arr=[10,3,6,5,14,8]
Solution().merge_sort(arr)
```


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-16-90ace2e58113> in <module>()
          1 arr=[10,3,6,5,14,8]
    ----> 2 Solution().merge_sort(arr)
    

    <ipython-input-15-6e3e8c4fe4b3> in merge_sort(self, arr)
          8             left_arr = arr[0:mid]    #左半邊的array
          9             right_arr = arr[mid:]    #右半邊的array
    ---> 10             Solution().merge_sort(left_arr)      #重複呼叫merge_sort，直到array不能再分為止
         11             Solution().merge_sort(right_arr)
         12 


    <ipython-input-15-6e3e8c4fe4b3> in merge_sort(self, arr)
          9             right_arr = arr[mid:]    #右半邊的array
         10             Solution().merge_sort(left_arr)      #重複呼叫merge_sort，直到array不能再分為止
    ---> 11             Solution().merge_sort(right_arr)
         12 
         13             i = 0  #left array的index


    <ipython-input-15-6e3e8c4fe4b3> in merge_sort(self, arr)
          9             right_arr = arr[mid:]    #右半邊的array
         10             Solution().merge_sort(left_arr)      #重複呼叫merge_sort，直到array不能再分為止
    ---> 11             Solution().merge_sort(right_arr)
         12 
         13             i = 0  #left array的index


    KeyboardInterrupt: 


到這裡我重新思考了mergesort的邏輯。主要需要一個把array進行divide的function，divide到不能再分為止；另外需要一個把被divide的array再繼續重新合併，並且是邊比大小邊合併，直到合併成一個array。###然後這裡發現if j == None那邊的邏輯還是有誤，如果都比較完了，


```python
class Solution():
    def merge(self,arr,front,mid,end):
            i = 0  #left array的index
            j = 0  #right array的index
            m = 0 #array的index
            while i < len(left_arr) and j < len(right_arr):    #當左右兩個array的index在正確範圍的時候
                if left_arr[i] < right_arr[j]: #比較左右array的指定index大小(從頭開始比較)
                    arr[m] = left_arr[i] #若左邊array的值比右邊array大，則把比較後的值更換到最初始array的對應index的值
                    i += 1                  #index加一，進行下一個值的比較
                    m += 1                #index加一，記錄下一個即將被更換的位置。
                else:
                    arr[m] = right_arr[j]
                    j += 1
                    m += 1
            
            if j == None:            #此處要考慮當j或i跑到index外面的時候，剩下一邊的array(左或右)的最後一個值直接更換到原array的最後一個位置裡
                while i < len(left_arr):
                    arr[m] = left_arr[i]
                    i +=1
                    m +=1
            
            if i == None:
                while j <len(right_arr):
                    arr[m] = right_arr[j]
                    j += 1
                    m += 1
        
        
    def merge_sort(self,arr,front,end):
         if len(arr) ==1:
            return arr
        
         while len(arr) >1:
            mid = len(arr)//2  #這裡的//是省略小數，方便取中點
            left_arr = arr[0:mid]    #左半邊的array
            right_arr = arr[mid:]    #右半邊的array
            Solution().merge_sort(left_arr)      #重複呼叫merge_sort，直到array不能再分為止
            Solution().merge_sort(right_arr)
            
          
```

如果右邊array的idex初始設定為0，似乎十分不方便。直接用原array的index來表示或許更好些；並且mid如果用len(arr)-2表示的話，如果array被divide，這裡的arr依舊調用的測試input進去的array而不是被divide的array(之前寫heapsort的血淚教訓，還需要另外設定變數才可)。所以如果是用頭跟尾的index來記錄或許更方便些。


```python
class Solution():
    def merge(self,arr,front,mid,end):
            i = 0  #left array的index
            j = mid + 1  #right array的index
            m = 0 #array的index
            while i < len(left_arr) and j < len(right_arr):    #當左右兩個array的index在正確範圍的時候
                if left_arr[i] < right_arr[j]: #比較左右array的指定index大小(從頭開始比較)
                    arr[m] = left_arr[i] #若左邊array的值比右邊array大，則把比較後的值更換到最初始array的對應index的值
                    i += 1                  #index加一，進行下一個值的比較
                    m += 1                #index加一，記錄下一個即將被更換的位置。
                else:
                    arr[m] = right_arr[j]
                    j += 1
                    m += 1
            
            if j == None:            #此處要考慮當j或i跑到index外面的時候，剩下一邊的array(左或右)的最後一個值直接更換到原array的最後一個位置裡
                while i < len(left_arr):
                    arr[m] = left_arr[i]
                    i +=1
                    m +=1
            
            if i == None:
                while j <len(right_arr):
                    arr[m] = right_arr[j]
                    j += 1
                    m += 1
        
        
    def merge_sort(self,arr,front,end):
         if len(arr) ==1:
            return arr
        
         while len(arr) >1:
            mid = front+end//2  #這裡的//是省略小數，方便取中點
            left_arr = arr[0:mid]    #左半邊的array，不包括mid
            right_arr = arr[mid:]    #右半邊的array，包括mid
            Solution().merge_sort(left_arr)      #重複呼叫merge_sort，直到array不能再分為止
            Solution().merge_sort(right_arr)
            
          
```

寫來寫去感覺還是設定空array的做法比較容易TAT......不然還要設定left_arr和right_arr，寫到這裡又想了好久要怎麼優化程式碼。這邊不想用append，所以我用了比較笨的方法，先把原array的值複製到設定好的空array裡面，然後再比大小把比較後的值替換到設定的array裡面，這樣能保證設定的array和測試的array的長度相同。


```python
class Solution():
    def MergeSingle(self,arr,front,mid,end):
            i = front      #left array的index
            j = mid + 1  #right array的index
            
            m = front #array的index
            while m <= end:     #這裡是把array的值複製到空array的裡面
                a[m] = arr[m]     
                m+=1
            
            while i<mid and j<end:
                if a[i]<a[j]:
                    arr[m] = a[i]
                    i+=1
                    m+=1
                    
                else:
                    arr[m] = a[j]
                    j+=1
                    m+=1
                
            if j == None:            
                while i < mid:
                    arr[m] = a[i]
                    i +=1
                    m +=1
            
            if i == None:
                while j <end:
                    arr[m] = a[j]
                    j += 1
                    m += 1
            
        
        
    def merge_sort(self,arr,front,end):
         if len(arr) ==1:
            return arr
        
         while len(arr) >1:
            mid = front+end//2  #這裡的//是省略小數，方便取中點
            Solution().merge_sort(arr,front,mid)    #遞迴左半邊的array
            Solution().merge_sort(arr,mid+1,end)    #遞迴右半邊的array
            Solution().MergeSingle(arr,front,mid,end)      #單趟merge
            
          
```


```python
arr=[10,3,6,5,14,8]
Solution().merge_sort(arr)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-21-90ace2e58113> in <module>()
          1 arr=[10,3,6,5,14,8]
    ----> 2 Solution().merge_sort(arr)
    

    TypeError: merge_sort() missing 2 required positional arguments: 'front' and 'end'


這裡又遇到另外的問題...因為最後的merge_sort只需要一個arr，沒有其他的變數，而我目前還有front、mid、end，要再想辦法TOT。。。。
還有我真的是太愚蠢了，同學幫我指正，j++直到超出範圍，但不是等於None....
這裡也不可以用extend，a的值已經是原array的值，再extend會增加value。


```python
class Solution():
    def MergeSingle(self,arr,front,mid,end):

            front=0
            end = len(arr)-1
            i = front          #left array的index
            j = mid + 1      #right array的index
            
            m = front #array的index
            while m <= end:     #這裡是把array的值複製到空array的裡面
                a[m] = arr[m]     
                m+=1
            
            while i<mid and j<end:
                if arr[i]<arr[j]:
                    a[m] = arr[i]
                    i+=1
                    m+=1
                    
                else:
                    a[m] = arr[j]
                    j+=1
                    m+=1
                
           
            if j==end:
                a. extend(arr[i,mid])
            else:
                a. extend(arr[mid+1,end])
            
        
    def merge_sort(self,arr,front,end):
        if len(arr) ==1:
            return arr
        front = 0
        end = len(arr)-1
        
        while len(arr) >1:
            mid = front+end//2  #這裡的//是省略小數，方便取中點
            Solution().merge_sort(arr,front,mid)    #遞迴左半邊的array
            Solution().merge_sort(arr,mid+1,end)    #遞迴右半邊的array
            Solution().MergeSingle(arr,front,mid,end)      #單趟merge
            
          
```


```python
arr=[10,3,6,5,14,8]
Solution().merge_sort(arr)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-37-90ace2e58113> in <module>()
          1 arr=[10,3,6,5,14,8]
    ----> 2 Solution().merge_sort(arr)
    

    TypeError: merge_sort() missing 2 required positional arguments: 'front' and 'end'



```python
我向其他同學求救。。。。。。。。。。。。
這裡乾脆直接用mergesingle只對設定的array進行拆分，然後還是和最初一樣直接設定ij的初始值為0
還有。。。我最後還是用了append  TAT.....
同學告訴我還要return值 不然結果會沒有，我再補上了return
```


```python
class Solution():
    def MergeSingle(self,left_arr,right_arr):
            
            i = 0          #left array的index
            j = 0          #right array的index
            a=[]           #設定的空list
            mid=len(left_arr)       #left array的最大index
            end=len(right_arr)     #right array的最大index
            while i<mid and j<end:     #在i和j都在index範圍裡的時候比較
                if left_arr[i]<=right_arr[j]:
                    a.append(left_arr[i])      #如果左邊array的值比右邊array還要小，則把當前左邊array的append進a裡面
                    i+=1                      #i的index向後移一個，繼續比較
                else:
                    a.append(right_arr[j])
                    j+=1
                
           
            if j==end:                    #如果j走到end的時候，代表j已經比完了，那個直接把剩下的left array的值放進去
                a= a+left_arr[i:]
            return a
            
            if i==end:
                a= a+right_arr[j:]
            return a
            
        
        
    def merge_sort(self,arr):
        if len(arr)<=1:
            return arr
        left=arr[:mid]
        right=arr[mid:]
        mid = len(arr)//2  #這裡的//是省略小數，方便取中點
        arr1=self.merge_sort(left)
        arr2=self.merge_sort(right)
        return self.MergeSingle(arr1,arr2)
```


```python
arr=[10,3,6,5,14,8]
Solution().merge_sort(arr)
```


    ---------------------------------------------------------------------------

    UnboundLocalError                         Traceback (most recent call last)

    <ipython-input-58-90ace2e58113> in <module>()
          1 arr=[10,3,6,5,14,8]
    ----> 2 Solution().merge_sort(arr)
    

    <ipython-input-57-8e7db1c39ecb> in merge_sort(self, arr)
         29         if len(arr)<=1:
         30             return arr
    ---> 31         left=arr[:mid]
         32         right=arr[mid:]
         33         mid = len(arr)//2  #這裡的//是省略小數，方便取中點


    UnboundLocalError: local variable 'mid' referenced before assignment


我的眼睛要脫窗了。。。。。。。。

原來不可以直接把left right的範圍預先設定好


```python
class Solution():
    def MergeSingle(self,left_arr,right_arr):
            
            i = 0          #left array的index
            j = 0          #right array的index
            a=[]           #設定的空list
            mid=len(left_arr)       #left array的最大index
            end=len(right_arr)     #right array的最大index
            while i<mid and j<end:     #在i和j都在index範圍裡的時候比較
                if left_arr[i]<=right_arr[j]:
                    a.append(left_arr[i])      #如果左邊array的值比右邊array還要小，則把當前左邊array的append進a裡面
                    i+=1                      #i的index向後移一個，繼續比較
                else:
                    a.append(right_arr[j])
                    j+=1
                
           
            if j==end:                     #如果j走到end的時候，代表j已經比完了，那個直接把剩下的left array的值放進去
                a= a+ left_arr[i:]
            else:                           #i也同理
                a= a+ right_arr[j:]
            return a
            
        
        
    def merge_sort(self,arr):
        if len(arr)<=1:         #如果array長度不大於1，則直接回傳，默認已經排序
            return arr
        
        
        mid = len(arr)//2  #這裡的//是省略小數，方便取中點
        arr1=Solution().merge_sort(arr[:mid])  #遞迴左半邊的array
        arr2=Solution().merge_sort(arr[mid:]) #遞迴左半邊的array
        return Solution().MergeSingle(arr1,arr2)#單趟merge
```


```python
arr=[10,3,6,5,14,8]
Solution().merge_sort(arr)
```




    [3, 5, 6, 8, 10, 14]




```python

```
