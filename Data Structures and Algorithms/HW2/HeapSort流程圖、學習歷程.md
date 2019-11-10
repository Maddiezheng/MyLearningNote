
方法：
1. 先構建一個max heap。滿足的狀況是父節點永遠比子節點大。
2. 然後重複地把最大值取出來和最後一個值交換位置，並且交換後的最大值不參與再構建max heap。

max heapify的功能是維護最大堆的性質。如果父節點與子節點進行交換，那麼要對交換後的subtree再進行檢查，看是否有滿足最大堆的性質。
                
                
        

參考資料：

http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html

https://www.geeksforgeeks.org/python-program-for-heap-sort/


流程圖：

![](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/heapsort流程圖.png)

寫的cell太多，就不一一描述，針對後半段的cell進行了一些闡述


```python
class Solution():
    
    def MaxAdjustment(self,arr,n):            #在這裏構建一個Max Heap
        N = len(arr)
        
        for n in len(arr):
            left_child=2*n                     #左邊child的index
            right_child=2*n+1                #右邊child的index
            parent = n
            if arr[left_child] > arr[right_child]:           #如果右邊沒有child或左邊的child比右邊的大，則maxnode是left_child
                max = left_child         
            else:
                max = right_child                                                               #反之，右邊較大則maxnode為right_child
                
            if arr[max] > arr[parent]:
                arr[n],arr[max] = arr[max],arr[parent]
                
                MaxAdjustment(arr,max)  
                
                
```

此處的error：缺少一個必須的位置參數“n”


```python
arr = [7,10,12,19,30,26,20,25,18]
p = Solution()
p.MaxAdjustment(arr)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-29-fcf43e672da1> in <module>()
          1 arr = [7,10,12,19,30,26,20,25,18]
          2 p = Solution()
    ----> 3 p.MaxAdjustment(arr)
    

    TypeError: MaxAdjustment() missing 1 required positional argument: 'n'


第二遍：


```python
class Solution():
    
    def MaxAdjustment(self,arr,n):            #在這裏構建一個Max Heap
            N = len(arr)
        
            left_child=2*n                     #左邊child的index
            right_child=2*n+1                #右邊child的index
            parent = n
            if left_child < N && arr[left_child] > arr[right_child]:           #如果右邊沒有child或左邊的child比右邊的大，則maxnode是left_child
                max = left_child         
            elif right_child == None:
                max = left_child
            else:
                max = right_child                                                               #反之，右邊較大則maxnode為right_child
                
            if arr[max] > arr[n]:
                arr[n],arr[max] = arr[max],arr[n]
                
                return MaxAdjustment(arr,max)            #此時parent的index變為max，檢查新的subtree是否符合maxheap
            
        def BuildHeap()：
              for i = N/2:
                return MaxAdjustment(arr,i,N)
```


      File "<ipython-input-30-e8c7a8777d7d>", line 9
        if left_child < N && arr[left_child] > arr[right_child]:           #如果右邊沒有child或左邊的child比右邊的大，則maxnode是left_child
                           ^
    SyntaxError: invalid syntax




```python
arr = [7,10,12,19,30,26,20,25,18]
p = Solution()
p.MaxAdjustment(arr,1)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-31-e244d3179d82> in <module>()
          1 arr = [7,10,12,19,30,26,20,25,18]
          2 p = Solution()
    ----> 3 p.MaxAdjustment(arr,1)
    

    <ipython-input-28-117e9c37ac24> in MaxAdjustment(self, arr, n)
          4         N = len(arr)
          5 
    ----> 6         for n in len(arr):
          7             left_child=2*n                     #左邊child的index
          8             right_child=2*n+1                #右邊child的index


    TypeError: 'int' object is not iterable



```python
class Solution():
    
    def MaxAdjustment(self,arr,n):            #在這裏構建一個Max Heap
            N = len(arr)
        
            left_child=2*n                     #左邊child的index
            right_child=2*n+1                #右邊child的index
            parent = n
            if arr[left_child] > arr[right_child]:           #如果右邊沒有child或左邊的child比右邊的大，則maxnode是left_child
                max_node = left_child         
            elif right_child == None:
                max_node = left_child
            else:
                max_node = right_child                                                               #反之，右邊較大則maxnode為right_child
                
            if arr[max_node] > arr[n]:
                arr[n],arr[max_node] = arr[max_node],arr[n]
                
                return MaxAdjustment(arr,max_node)            #此時parent的index變為max，檢查新的subtree是否符合maxheap
            
        
```


```python
arr = [7,10,12,19,30,26,20,25,18]
MaxAdjustment(arr,1)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-33-f38f9fdfb442> in <module>()
          1 arr = [7,10,12,19,30,26,20,25,18]
    ----> 2 MaxAdjustment(arr,1)
    

    NameError: name 'MaxAdjustment' is not defined



```python
class Solution():
    
    def MaxAdjustment(self,arr,n):            #在這裏構建一個Max Heap
            N = len(arr)
        
            left_child=2*n                     #左邊child的index
            right_child=2*n+1                #右邊child的index
            parent = n
            if left_child < len(arr) and arr[left_child] > arr[parent]:
                max_node = left_child
                else:
                    max_node = parent
            if right < len(arr) and arr[right_child] > arr[largest]:
                max_node = right_child
                
            if max_node != parent:
                arr[parent],arr[max_node] = arr[max_node],A[parent]
                MaxAdjustment(arr,max_node)
```


      File "<ipython-input-34-7f9ac4a7dfb8>", line 11
        else:
           ^
    SyntaxError: invalid syntax




```python
class Solution():
    
    def MaxAdjustment(self,arr,n):            #在這裏構建一個Max Heap
            N = len(arr)
        
            left_child=2*n                     #左邊child的index
            right_child=2*n+1                #右邊child的index
            parent = n
            
            if left_child > N:                  #排除left_node不存在的情況
                return
            
            if arr[left_child] > arr[right_child] && arr[left_child] > arr[parent]:           #若left_child和parent、right_比較後是最大的，則maxnode是left_child
                max_node = left_child         
            elif arr[right_child] > arr[left_child] && arr[right_child] > arr[parent]:
                max_node = right_child
            else:
                max_node = parent                                                               #反之，右邊較大則maxnode為right_child
                
            if arr[max_node] > arr[parent]:
                arr[parent],arr[max_node] = arr[max_node],arr[parent]
                
                return MaxAdjustment(arr,max_node)            #此時parent的index變為max，檢查新的subtree是否符合maxheap
            
```


      File "<ipython-input-35-bd0046f0bc86>", line 13
        if arr[left_child] > arr[right_child] && arr[left_child] > arr[parent]:           #若left_child和parent、right_比較後是最大的，則maxnode是left_child
                                               ^
    SyntaxError: invalid syntax




```python
class Solution():
    def MaxAdjustment(self,arr,n):            #在這裏構建一個Max Heap
            N = len(arr)
        
            left_child=2*n                     #左邊child的index
            right_child=2*n+1                #右邊child的index
            parent = n

            if arr[left_child] > arr[n]:           #若left_child和parent、right_比較後是最大的，則maxnode是left_child
                max_node = left_child         
            elif arr[right_child] > arr[n]:
                max_node = right_child
            else:
                max_node = parent                                                               #反之，右邊較大則maxnode為right_child
                
            if arr[max_node] > arr[n]:
                arr[n],arr[max_node] = arr[max_node],arr[n]
                
                return self.MaxAdjustment(arr,max_node)            #此時parent的index變為max，檢查新的subtree是否符合maxheap
            
```


```python
arr = [7,10,12,19,30,26,20,25,18]
p = Solution()
p.MaxAdjustment(arr,1)
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-37-e244d3179d82> in <module>()
          1 arr = [7,10,12,19,30,26,20,25,18]
          2 p = Solution()
    ----> 3 p.MaxAdjustment(arr,1)
    

    <ipython-input-36-7ee13b41abae> in MaxAdjustment(self, arr, n)
         17                 arr[n],arr[max_node] = arr[max_node],arr[n]
         18 
    ---> 19                 return self.MaxAdjustment(arr,max_node)            #此時parent的index變為max，檢查新的subtree是否符合maxheap
         20 


    <ipython-input-36-7ee13b41abae> in MaxAdjustment(self, arr, n)
         17                 arr[n],arr[max_node] = arr[max_node],arr[n]
         18 
    ---> 19                 return self.MaxAdjustment(arr,max_node)            #此時parent的index變為max，檢查新的subtree是否符合maxheap
         20 


    <ipython-input-36-7ee13b41abae> in MaxAdjustment(self, arr, n)
         17                 arr[n],arr[max_node] = arr[max_node],arr[n]
         18 
    ---> 19                 return self.MaxAdjustment(arr,max_node)            #此時parent的index變為max，檢查新的subtree是否符合maxheap
         20 


    <ipython-input-36-7ee13b41abae> in MaxAdjustment(self, arr, n)
          7             parent = n
          8 
    ----> 9             if arr[left_child] > arr[n]:           #若left_child和parent、right_比較後是最大的，則maxnode是left_child
         10                 max_node = left_child
         11             elif arr[right_child] > arr[n]:


    IndexError: list index out of range



```python
class Solution():
    def MaxAdjustment(self,arr,n):            #在這裏構建一個Max Heap
            N = len(arr)
        
            left_child=2*n                     #左邊child的index
            right_child=2*n+1                #右邊child的index
            parent = n

            if left_child <N and arr[left_child] > arr[n]:           #若left_child和parent、right_比較後是最大的，則maxnode是left_child
                max_node = left_child         
            elif right_child < N and arr[right_child] > arr[n]:
                max_node = right_child
            else:
                max_node = parent                                                               #反之，右邊較大則maxnode為right_child
                
            if arr[max_node] > arr[n]:
                arr[n],arr[max_node] = arr[max_node],arr[n]
                
                return self.MaxAdjustment(arr,max_node)            #此時parent的index變為max，檢查新的subtree是否符合maxheap
```


```python
arr = [1,2,3,4,5]
p = Solution()
p.MaxAdjustment(arr,4)
print(arr)
```

    [1, 2, 3, 4, 5]



```python
class Solution():
    def heapBuild(self,arr):     
        N = len(arr)
        for i in range(N,0,-1):
            current_Index = i #當前index為i
            parent_Index = (current_Index - 1)//2   #parentnode的index  這裡用//是因為遇到偶數時可以省略小數，找到parentnode的index
            while arr[current_Index] > arr[parent_Index]:
                arr[current_Index],arr[parent_Index] = arr[parent_Index],arr[current_Index]       #交換current_Index和parent的位置
                current_Index = parent_Index                                     #當前node的index變為其本來的parentnode的index
                parent_Index = (current_Index - 1)//2                         #原本parentnode的index變為原本當前node的index
            
```


```python
arr = [7,10,12,19,30,26]
q = Solution()
q.heapBuild(arr)
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-41-baf3f13abe0e> in <module>()
          1 arr = [7,10,12,19,30,26]
          2 q = Solution()
    ----> 3 q.heapBuild(arr)
    

    <ipython-input-40-5fc8883bcb55> in heapBuild(self, arr)
          5             current_Index = i #當前index為i
          6             parent_Index = (current_Index - 1)//2   #parentnode的index  這裡用//是因為遇到偶數時可以省略小數，找到parentnode的index
    ----> 7             while arr[current_Index] > arr[parent_Index]:
          8                 arr[current_Index],arr[parent_Index] = arr[parent_Index],arr[current_Index]       #交換current_Index和parent的位置
          9                 current_Index = parent_Index                                     #當前node的index變為其本來的parentnode的index


    IndexError: list index out of range


先建立一個heap，我這裡是選擇用Max heap：


```python
class Solution():
    def heapBuild(self,arr):     #建立max heap，currentnode從下往上依次和parentnode比較
        N = len(arr)
        for i in range(N-1,0,-1):
            current_Index = i #當前index為i
            parent_Index = (current_Index - 1)//2   #parentnode的index  這裡用//是因為遇到偶數時可以省略小數，找到parentnode的index
            if arr[current_Index] > arr[parent_Index]:
                arr[parent_Index],arr[current_Index] = arr[current_Index],arr[parent_Index]       #交換current_Index和parent的位置
        return self.heapBuild(arr)
```


```python
arr = [7,10,12,19,30,26,20,25]
q = Solution()
q.heapBuild(arr)
```


    ---------------------------------------------------------------------------

    RecursionError                            Traceback (most recent call last)

    <ipython-input-43-574490d1f4b5> in <module>()
          1 arr = [7,10,12,19,30,26,20,25]
          2 q = Solution()
    ----> 3 q.heapBuild(arr)
    

    <ipython-input-42-47002de85d13> in heapBuild(self, arr)
          7             if arr[current_Index] > arr[parent_Index]:
          8                 arr[parent_Index],arr[current_Index] = arr[current_Index],arr[parent_Index]       #交換current_Index和parent的位置
    ----> 9         return self.heapBuild(arr)
    

    ... last 1 frames repeated, from the frame below ...


    <ipython-input-42-47002de85d13> in heapBuild(self, arr)
          7             if arr[current_Index] > arr[parent_Index]:
          8                 arr[parent_Index],arr[current_Index] = arr[current_Index],arr[parent_Index]       #交換current_Index和parent的位置
    ----> 9         return self.heapBuild(arr)
    

    RecursionError: maximum recursion depth exceeded in comparison


第一遍：


```python
class Solution():
    def MaxAdjustment(self,arr,n):            
            N = len(arr)
    
            left_child=2*n+1                    #左邊child的index
            right_child=2*n+2             #右邊child的index
            parent = n
            while left_child < N:            #left_child存在的情況下才會進行比較
                if arr[left_child] > arr[parent] and arr[left_child] > arr[right_child]:
                    max_node = left_child
                    arr[parent],arr[left_child] = arr[left_child],arr[parent]
                elif right_child < N and arr[right_child] > arr[left_child] and arr[right_child] > arr[parent]:
                    max_node = right_child
                    arr[parent],arr[right_child] = arr[right_child],arr[parent]
                else:
                    max_node = parent
                
                return self.MaxAdjustment(arr,max_node)            #此時parent的index變為max，檢查新的subtree是否符合maxheap
```


```python
arr = [7,10,12,19,30,26,20,25]
p = Solution()
p.MaxAdjustment(arr,0)
arr
```

第二遍：


```python
class Solution():
    
    def heapBuild(self,arr):     #建立max heap，currentnode從下往上依次和parentnode比較
        N = len(arr)
        for i in range(N-1,0,-1):
            current_Index = i #當前index為i，從後往前遍歷
            parent_Index = (current_Index - 1)//2   #parentnode的index  這裡用//是因為遇到偶數時可以省略小數，找到parentnode的index
            if arr[current_Index] > arr[parent_Index]:
                arr[parent_Index],arr[current_Index] = arr[current_Index],arr[parent_Index]       #交換current_Index和parent的位置
    
    def MaxAdjustment(self,arr,n):    
        N = len(arr)
        left_child=2*n+1                    #左邊child的index
        right_child=2*n+2             #右邊child的index
        parent = n
        while left_child < N:            #left_child存在的情況下才會進行比較
            if arr[left_child] > arr[n] and arr[left_child] > arr[right_child]:
                max_node = left_child
                arr[parent],arr[left_child] = arr[left_child],arr[parent]
            elif right_child < N and arr[right_child] > arr[left_child] and arr[right_child] > arr[parent]:
                max_node = right_child
                arr[parent],arr[right_child] = arr[right_child],arr[parent]
            else:
                max_node = parent
            return self.MaxAdjustment(arr,max_node)            #此時parent的index變為max，檢查新的subtree是否符合maxheap
        
    def HeapSort(self,arr):
        N = len(arr)
        self.heapBuild(arr)
        while N >1:  
            arr[0],arr[-1] = arr[-1],arr[0]
            self.MaxAdjustment(arr,0)
    
    
    
```


```python
arr = [7,10,12,19,30,26,20,25]
m = Solution()
m.HeapSort(arr)

```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-45-7a9b796ce99d> in <module>()
          1 arr = [7,10,12,19,30,26,20,25]
          2 m = Solution()
    ----> 3 m.HeapSort(arr)
    

    <ipython-input-44-7f359ac84412> in HeapSort(self, arr)
         30         while N >1:
         31             arr[0],arr[-1] = arr[-1],arr[0]
    ---> 32             self.MaxAdjustment(arr,0)
         33 
         34 


    <ipython-input-44-7f359ac84412> in MaxAdjustment(self, arr, n)
         23             else:
         24                 max_node = parent
    ---> 25             return self.MaxAdjustment(arr,max_node)            #此時parent的index變為max，檢查新的subtree是否符合maxheap
         26 
         27     def HeapSort(self,arr):


    <ipython-input-44-7f359ac84412> in MaxAdjustment(self, arr, n)
         23             else:
         24                 max_node = parent
    ---> 25             return self.MaxAdjustment(arr,max_node)            #此時parent的index變為max，檢查新的subtree是否符合maxheap
         26 
         27     def HeapSort(self,arr):


    <ipython-input-44-7f359ac84412> in MaxAdjustment(self, arr, n)
         15         parent = n
         16         while left_child < N:            #left_child存在的情況下才會進行比較
    ---> 17             if arr[left_child] > arr[n] and arr[left_child] > arr[right_child]:
         18                 max_node = left_child
         19                 arr[parent],arr[left_child] = arr[left_child],arr[parent]


    IndexError: list index out of range



```python
class Solution():
    def MaxAdjustment(self,arr,n):            
            N = len(arr)
    
            left_child=2*n+1                    #左邊child的index
            right_child=2*n+2             #右邊child的index
            parent = n
            while left_child < N:            #left_child存在的情況下才會進行比較
                if arr[left_child] > arr[n] and arr[left_child] > arr[right_child]:
                    max_node = left_child
                    arr[parent],arr[left_child] = arr[left_child],arr[parent]
                elif arr[parent] > arr[left_child] and arr[parent] > arr[right_chile]:
                    max_node = parent
                else:
                    max_node = right_child
                
                return self.MaxAdjustment(arr,max_node)            #此時parent的index變為max，檢查新的subtree是否符合maxheap
```


```python
arr = [7,10,12,19,30,26,20,25]
p = Solution()
p.MaxAdjustment(arr,1)
```


```python
p
```




    <__main__.Solution at 0x1062c3be0>




```python
class Solution():
    def MaxAdjustment(self,arr,n):            
            N = len(arr)
    
            left_child=2*n+1                    #左邊child的index
            right_child=2*n+2             #右邊child的index
            parent = n
            while left_child < N:            #left_child存在的情況下才會進行比較
                if arr[left_child] > arr[parent]:
                    max_node = left_child
                else:
                    max_node = parent
                    
            while right_child < N:
                if arr[right_child] > arr[parent]:
                    max_node = right_child
                else:
                    max_node = parent
                    
            if arr[parent] < arr[max_node]:
                arr[parent],arr[max_node] = arr[max_node], arr[parent]
                
                return self.MaxAdjustment(arr,max_node)            #此時parent的index變為max，檢查新的subtree是否符合maxheap
```


```python
arr = [7,10,12,19,30,26,20,25]
p = Solution()
p.MaxAdjustment(arr,0)
arr
```


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-50-95c5562c4eaa> in <module>()
          1 arr = [7,10,12,19,30,26,20,25]
          2 p = Solution()
    ----> 3 p.MaxAdjustment(arr,0)
          4 arr


    <ipython-input-49-76e616dfca71> in MaxAdjustment(self, arr, n)
          6             right_child=2*n+2             #右邊child的index
          7             parent = n
    ----> 8             while left_child < N:            #left_child存在的情況下才會進行比較
          9                 if arr[left_child] > arr[parent]:
         10                     max_node = left_child


    KeyboardInterrupt: 



```python
p
```


```python
class Solution():
    def MaxAdjustment(self,arr,n):            
            N = len(arr)
            global max_node
            left_child=2*n+1                    #左邊child的index
            right_child=2*n+2             #右邊child的index
            parent = n
            
            if left_child < N and arr[left_child] > arr[right_child]:             #left_child存在的情況下才會進行比較
                max_node = left_child
                    
            if right_child < N and arr[right_child] > arr[left_child]:
                    max_node = right_child
                    
            if arr[parent] < arr[max_node]:
                arr[parent],arr[max_node] = arr[max_node], arr[parent]
                
                return self.MaxAdjustment(arr,max_node)            #此時parent的index變為max，檢查新的subtree是否符合maxheap
```


```python
arr = [7,10,12,19,30,26,20,25]
p = Solution()
p.MaxAdjustment(arr,0)
arr
```




    [12, 10, 26, 19, 30, 7, 20, 25]




```python
class Solution():
    
    def heapBuild(self,arr):     #建立max heap，currentnode從下往上依次和parentnode比較
        N = len(arr)
        for i in range(N-1,0,-1):
            current_Index = i #當前index為i
            parent_Index = (current_Index - 1)//2   #parentnode的index  這裡用//是因為遇到偶數時可以省略小數，找到parentnode的index
            if arr[current_Index] > arr[parent_Index]:
                arr[parent_Index],arr[current_Index] = arr[current_Index],arr[parent_Index]       #交換current_Index和parent的位置
        
    def HeapSort(self,arr):
        N = len(arr)
        self.heapBuild(arr)
       
    
    
    
```


```python
arr = [30,26,7,25,10,20,12,19]
p = Solution()
p.HeapSort(arr)
arr
```




    [30, 26, 20, 25, 10, 12, 7, 19]




```python
arr = [30,26,20,25,10,12,7,19]
p = Solution()
p.HeapSort(arr)
arr
```




    [30, 26, 20, 25, 10, 12, 7, 19]




```python
arr = [7,10,12,19,30,26,20,25]
p = Solution()
p.HeapSort(arr)
arr
```




    [30, 26, 7, 25, 10, 20, 12, 19]




```python
class Solution():
    
    def heapBuild(self,arr):     #建立max heap，currentnode從下往上依次和parentnode比較
        N = len(arr)
        for i in range(N-1,0,-1):
            current_Index = i #當前index為i
            parent_Index = (current_Index - 1)//2   #parentnode的index  這裡用//是因為遇到偶數時可以省略小數，找到parentnode的index
            if arr[current_Index] > arr[parent_Index]:
                arr[parent_Index],arr[current_Index] = arr[current_Index],arr[parent_Index]       #交換current_Index和parent的位置
    
    def MaxAdjustment(self,arr,n, N):    
        
        left_child=2*n+1                    #左邊child的index
        right_child=2*n+2             #右邊child的index
        parent = n
        while left_child < N:            #left_child存在的情況下才會進行比較
            if arr[left_child] > arr[n] and arr[left_child] > arr[right_child]:
                max_node = left_child
                arr[parent],arr[left_child] = arr[left_child],arr[parent]
            elif right_child < N and arr[right_child] > arr[left_child] and arr[right_child] > arr[parent]:
                max_node = right_child
                arr[parent],arr[right_child] = arr[right_child],arr[parent]
            else:
                max_node = parent
                            #此時parent的index變為max，檢查新的subtree是否符合maxheap
        
    def HeapSort(self,arr):
        N = len(arr)
        self.heapBuild(arr)
        while N >1:  
            arr[0],arr[-1] = arr[-1],arr[0]
            N -= 1
            self.MaxAdjustment(arr,0,N)
    
    
```


```python
arr = [7,10,12,19,30,26,20,25]
p = Solution()
p.HeapSort(arr)
arr
```


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-60-46e1d9fc81bd> in <module>()
          1 arr = [7,10,12,19,30,26,20,25]
          2 p = Solution()
    ----> 3 p.HeapSort(arr)
          4 arr


    <ipython-input-57-d439ac09968a> in HeapSort(self, arr)
         31             arr[0],arr[-1] = arr[-1],arr[0]
         32             N -= 1
    ---> 33             self.MaxAdjustment(arr,0,N)
         34 
         35 


    <ipython-input-57-d439ac09968a> in MaxAdjustment(self, arr, n, N)
         22                 arr[parent],arr[right_child] = arr[right_child],arr[parent]
         23             else:
    ---> 24                 max_node = parent
         25                             #此時parent的index變為max，檢查新的subtree是否符合maxheap
         26 


    KeyboardInterrupt: 



```python
class Solution():
    def HeapSort(self,arr,N):
        N = len(arr)
        for n=(N-1)/2


def Heapfy(self,arr,n,N):
    N = len(arr)
    left_child = 2*n+1
    right_child =2*n+2
    parent = n
    
    if parent > N:
        return
    
    if right_child < N and arr[parent] < arr[right_child]:
        max_node = right_child
    if left_child < N and arr[parent] < arr[left_child]:
        max_node = left_child
    if max_node != parent:
        if right_child < N and max_node = right_child:
            arr[parent],arr[right_child] = arr[right_child].arr[parent]
            self.Heapfy(arr,right_child,N)
        if left_child < N and max_node = left_child:
            arr[parent],arr[left_child] = arr[left_child],arr[parent]
            self.Heapfy(arr,left_child,N)
            
    
```


      File "<ipython-input-61-d182e2359eaf>", line 4
        for n=(N-1)/2
             ^
    SyntaxError: invalid syntax




```python
class Solution():
    def Heapfy(self,arr,n):
        global max_node
        N = len(arr)
        left_child = 2*n+1
        right_child =2*n+2
        parent = n
        
        
        if parent > N:
            return
        if right_child < N and arr[parent] < arr[right_child]:
            max_node = right_child
        else:
            max_node = parent
            
        if left_child < N and arr[parent] < arr[left_child]:
            max_node = left_child
        else:
            max_node = parent
            
        if max_node != parent:
            if right_child < N and max_node == right_child:
                arr[parent],arr[right_child] = arr[right_child].arr[parent]
                self.Heapfy(arr,right_child)
            if left_child < N and max_node == left_child:
                arr[parent],arr[left_child] = arr[left_child],arr[parent]
                self.Heapfy(arr,left_child)
            
```


```python
arr = [7,10,12,19,30,26,20,25]
p = Solution()
p.Heapfy(arr,0)
arr
```




    [10, 19, 12, 25, 30, 26, 20, 7]




```python
class Solution():
    def Heapfy(self,arr,n):
        global max_node
        N = len(arr)
        left_child = 2*n+1
        right_child =2*n+2
        parent = n
        
        
        if parent > N:
            return
        if right_child < N and arr[parent] < arr[right_child]:
            max_node = right_child
        else:
            max_node = parent
            
        if left_child < N and arr[parent] < arr[left_child]:
            max_node = left_child
        else:
            max_node = parent
            
        if max_node != parent:
            if right_child < N and arr[parent] < arr[right_child] :
                arr[parent],arr[right_child] = arr[right_child].arr[parent]
                self.Heapfy(arr,right_child)
            if left_child < N and arr[parent] < arr[left_child]:
                arr[parent],arr[left_child] = arr[left_child],arr[parent]
                self.Heapfy(arr,left_child)
```


```python
arr = [7,10,12,19,30,26,20,25]
p = Solution()
p.Heapfy(arr,0)
arr
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-65-7cc7aa5c0ac4> in <module>()
          1 arr = [7,10,12,19,30,26,20,25]
          2 p = Solution()
    ----> 3 p.Heapfy(arr,0)
          4 arr


    <ipython-input-64-ec0f1a4617c1> in Heapfy(self, arr, n)
         22         if max_node != parent:
         23             if right_child < N and arr[parent] < arr[right_child] :
    ---> 24                 arr[parent],arr[right_child] = arr[right_child].arr[parent]
         25                 self.Heapfy(arr,right_child)
         26             if left_child < N and arr[parent] < arr[left_child]:


    AttributeError: 'int' object has no attribute 'arr'



```python
class Solution():
    def MaxAdjustment(self,arr,n):            
            N = len(arr)
            global max_node
            left_child=2*n+1                    #左邊child的index
            right_child=2*n+2             #右邊child的index
            parent = n
            
            if left_child < N and arr[left_child] > arr[right_child]:             #left_child存在的情況下才會進行比較
                max_node = left_child
                    
            if right_child < N and arr[right_child] > arr[left_child]:
                    max_node = right_child
                    
            if arr[parent] < arr[max_node]:
                arr[parent],arr[max_node] = arr[max_node], arr[parent]
                
                return self.MaxAdjustment(arr,max_node)            #此時parent的index變為max，檢查新的subtree是否符合maxheap
```


```python
class Solution():
    def Heapfy(self,arr,n):
        global max_node
        N = len(arr)
        left_child = 2*n+1
        right_child =2*n+2
        parent = n
        
        
        if parent > N:
            return
        if right_child < N and arr[parent] < arr[right_child]:
            max_node = right_child
        else:
            max_node = parent
            
        if left_child < N and arr[parent] < arr[left_child]:
            max_node = left_child
        else:
            max_node = parent
            
        if max_node != parent:
            if right_child < N and max_node == right_child:
                arr[parent],arr[right_child] = arr[right_child].arr[parent]
                self.Heapfy(arr,right_child)
            if left_child < N and max_node == left_child:
                arr[parent],arr[left_child] = arr[left_child],arr[parent]
                self.Heapfy(arr,left_child)
            
```


```python
class Solution():
    
    def heapBuild(self,arr):     #建立max heap，currentnode從下往上依次和parentnode比較
        N = len(arr)
        for i in range(N-1,0,-1):
            current_Index = i #當前index為i，從後往前遍歷
            parent_Index = (current_Index - 1)//2   #parentnode的index  這裡用//是因為遇到偶數時可以省略小數，找到parentnode的index
            if arr[current_Index] > arr[parent_Index]:
                arr[parent_Index],arr[current_Index] = arr[current_Index],arr[parent_Index]       #交換current_Index和parent的位置
                
    def MaxAdjustment(self,arr,n,N):            
        global max_node
        left_child=2*n+1                    #左邊child的index
        right_child=2*n+2             #右邊child的index
        parent = n
        
        while left_child < N:
            if arr[left_child] > arr[right_child]:             #left_child存在的情況下才會進行比較
                max_node = left_child
            else:
                    max_node = right_child
            
            if max_node == parent:
                break
            
            if arr[parent] < arr[max_node]:
            arr[parent],arr[max_node] = arr[max_node], arr[parent]
            
            n = max_node
            left_child = 2*n+1
            right_child = 2*n+2
                           
    
    def HeapSort(self,arr):
        N = len(arr)
        self.heapBuild(arr)
        while N >1:  
            arr[0],arr[N-1] = arr[N-1],arr[0]
            N=N-1
            self.MaxAdjustment(arr,0,N)
    
    
```


      File "<ipython-input-68-af765c6daf2e>", line 27
        arr[parent],arr[max_node] = arr[max_node], arr[parent]
          ^
    IndentationError: expected an indented block




```python
arr = [7,10,12,19,30,26,20,25]
p = Solution()
p.HeapSort(arr)
arr
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-69-46e1d9fc81bd> in <module>()
          1 arr = [7,10,12,19,30,26,20,25]
          2 p = Solution()
    ----> 3 p.HeapSort(arr)
          4 arr


    AttributeError: 'Solution' object has no attribute 'HeapSort'



```python
class Solution():
    
    def heapBuild(self,arr):     #建立max heap，currentnode從下往上依次和parentnode比較
        N = len(arr)
        for i in range(N-1,0,-1):
            current_Index = i #當前index為i，從後往前遍歷
            parent_Index = (current_Index - 1)//2   #parentnode的index  這裡用//是因為遇到偶數時可以省略小數，找到parentnode的index
            if arr[current_Index] > arr[parent_Index]:
                arr[parent_Index],arr[current_Index] = arr[current_Index],arr[parent_Index]       #交換current_Index和parent的位置
                
    def MaxAdjustment(self,arr,n,N):            
        global max_node
        left_child=2*n+1                    #左邊child的index
        right_child=2*n+2             #右邊child的index
        parent = n
        
        while left_child < N:
            if right_child > N and arr[right_child] > arr[left_child]:             #left_child存在的情況下才會進行比較
                max_node = right_child
            else:
                    max_node = left_child
            
            if max_node == parent:
                break
            
            if arr[parent] < arr[max_node]:
                arr[parent],arr[max_node] = arr[max_node], arr[parent]
            
            n = max_node
            left_child = 2*n+1
            right_child = 2*n+2
                           
    
    def HeapSort(self,arr):
        N = len(arr)
        self.heapBuild(arr)
        while N >1:  
            arr[0],arr[N-1] = arr[N-1],arr[0]
            N=N-1
            self.MaxAdjustment(arr,0,N)
    
    
```


```python
arr = [7,10,12,19,30,26,20,25]
p = Solution()
p.HeapSort(arr)
arr
```




    [7, 10, 12, 19, 20, 25, 26, 30]




```python
class Solution():
    
    def heapBuild(self,arr):     #建立max heap，currentnode從下往上依次和parentnode比較
        N = len(arr)
        for i in range(N-1,0,-1):
            current_Index = i #當前index為i，從後往前遍歷
            parent_Index = (current_Index - 1)//2   #parentnode的index  這裡用//是因為遇到偶數時可以省略小數，找到parentnode的index
            while arr[current_Index] > arr[parent_Index]:
                arr[parent_Index],arr[current_Index] = arr[current_Index],arr[parent_Index]       #交換current_Index和parent的位置
                current_Index = parent_Index
                parent_Index = (current_Index -1)//2
                
                
    def MaxAdjustment(self,arr,n,N):            
        global max_node
        left_child=2*n+1                    #左邊child的index
        right_child=2*n+2             #右邊child的index
        parent = n
        
        while left_child < N:
            if right_child > N and arr[right_child] > arr[left_child]:             #left_child存在的情況下才會進行比較
                max_node = right_child
            else:
                    max_node = left_child
            
            if max_node == parent:
                break
            
            if arr[parent] < arr[max_node]:
                arr[parent],arr[max_node] = arr[max_node], arr[parent]
            
            n = max_node
            left_child = 2*n+1
            right_child = 2*n+2
                           
    
    def HeapSort(self,arr):
        N = len(arr)
        self.heapBuild(arr)
        while N >1:  
            arr[0],arr[N-1] = arr[N-1],arr[0]
            N=N-1
            self.MaxAdjustment(arr,0,N)
    
    
```


```python
arr = [7,10,12,19,30,26,20,25]
p = Solution()
p.HeapSort(arr)
arr
```




    [7, 20, 10, 12, 19, 25, 30, 26]




```python
def MaxAdjustment(self,arr,n,N):            
        global max_node
        left_child=2*n+1                    #左邊child的index
        right_child=2*n+2             #右邊child的index
        parent = n
        
        while left_child < N:
            if right_child > N and arr[right_child] > arr[left_child]:             #left_child存在的情況下才會進行比較
                max_node = right_child
            else:
                    max_node = left_child
            
            if max_node == parent:
                break
            
            if arr[parent] < arr[max_node]:
                arr[parent],arr[max_node] = arr[max_node], arr[parent]
            
            n = max_node
            left_child = 2*n+1
            right_child = 2*n+2
```


```python
arr = [30,26,7,25,10,12,20,19]
p = Solution()
p.MaxAdjustment(arr,0,8)
arr
```




    [30, 26, 7, 25, 10, 12, 20, 19]




```python
class Solution():
    def heapbuild(self,arr):
        N = len(arr)
        for n in range(N//2-1, -1, -1):
            self.MaxAdjustment(arr,n,N)
        
    def MaxAdjustment(self,arr,n,N):
        global max_node
        left_child = 2*n +1
        right_child = 2*n +2
        parent = n
        if left_child < N and arr[left_child] > arr[parent]:
            max_node = left_child
        else:
            max_node = parent
            
        if right_child < N and arr[right_child] > arr[parent]:
            max_node = right_child
        else:
            max_node = right_child
        
        if max_node != parent:
            arr[parent],arr[max_node] = arr[max_node],arr[parent]
            return self.MaxAdjustment(arr,max_node,N)
        
    def heapsort(self,arr):
        self.heapbuild(arr)
        N = len(arr)
        for i in range(N - 1, 0 ,-1):
            arr[0],arr[i] = arr[i],arr[0]
            N = N-1
            self.MaxAdjustment(arr,0,N)
                
```


```python
arr = [7,10,12,19,30,26,20,25]
p = Solution()
p.heapsort(arr)
arr
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-89-876d367cc09c> in <module>()
          1 arr = [7,10,12,19,30,26,20,25]
          2 p = Solution()
    ----> 3 p.heapsort(arr)
          4 arr


    <ipython-input-88-4121b0260e26> in heapsort(self, arr)
         25 
         26     def heapsort(self,arr):
    ---> 27         self.heapbuild(arr)
         28         N = len(arr)
         29         for i in range(N - 1, 0 ,-1):


    <ipython-input-88-4121b0260e26> in heapbuild(self, arr)
          3         N = len(arr)
          4         for n in range(N//2-1, -1, -1):
    ----> 5             self.MaxAdjustment(arr,n,N)
          6 
          7     def MaxAdjustment(self,arr,n,N):


    <ipython-input-88-4121b0260e26> in MaxAdjustment(self, arr, n, N)
         21 
         22         if max_node != parent:
    ---> 23             arr[parent],arr[max_node] = arr[max_node],arr[parent]
         24             return self.MaxAdjustment(arr,max_node,N)
         25 


    IndexError: list index out of range


一開始while迴圈內部邏輯搞錯，如果left_child和right_child同時大於max_node，子節點和父節點的位置交換會出現錯誤。例如678，這裡只會交換6和7，則排序為768


```python
class Solution():
    def maxheapify(self,arr,n,m):
        """
        維護max heap(因為最大值和最後一個值交換位置後會破壞原來的max heap結構)
        """
        left_child = 2*n+1          #左邊child的index
        right_child = 2*n+2                                  #右邊child的index,right_child = 2*n+2  
        max_node = n              #假設當前的max_node為parent
        
        while left_child < m or right_child < m:     #只有left_child存在的情況下才會進行判斷
            if arr[left_child] > arr[max_node]:    #比較leftchild和maxnode大小，若比maxnode大，則把其index更改為leftchild的index
                max_node = left_child
            elif arr[right_child] > arr[max_node]:   #只有rightchild存在的情況下才會進行判斷
                max_node = right_child                                                 #再比較rightchild和maxnode的大小。可能為原maxnode，可能為已經更改的maxnode
            else:
                break
        
        if max_node != n:             #如果max_node的index已經發生改變，則交換vaule的位置
            arr[n], arr[max_node] = arr[max_node],arr[n]
            Solution.maxheapify(arr,max_node,m)    #再對新的subtree進行檢查，看是否符合max heap的性質，直到找到最大值為止
        
    def heapbuild(self,arr):
        """
        構建max heap
        """
        m=len(arr)
        i = int(len(arr) / 2 - 1)             #非葉子節點的index。假設list有8個node，則非葉子節點的index為0，1，2，3
        while i >= 0:                  #從最後一個非葉子節點開始
            Solution.maxheapify(arr,i,m)
            i -= 1
    
    def heap_sort(self,arr):
        Solution.heapbuild(arr)
        m = len(arr)                                           
        while m >= 0:
            arr[0],arr[len(arr)-1] = arr[len(arr)-1],arr[0]
            m= m-1
            Solultion.maxheapify(arr,0,m)
```


```python
arr = [7,10,12,19,30,20,11]
p = Solution()
p.heap_sort(arr)
arr
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-91-5a4dc568dc5d> in <module>()
          1 arr = [7,10,12,19,30,20,11]
          2 p = Solution()
    ----> 3 p.heap_sort(arr)
          4 arr


    <ipython-input-90-ca721dfdb3c5> in heap_sort(self, arr)
         31 
         32     def heap_sort(self,arr):
    ---> 33         Solution.heapbuild(arr)
         34         m = len(arr)
         35         while m >= 0:


    TypeError: heapbuild() missing 1 required positional argument: 'arr'


這裡還是error，檢查發現maxheapify裡面的while迴圈的邏輯還是有錯，如果right_child不存在的話，while裡面的if不會去執行，最後連left_child也不會與max_node進行比較。


```python
class Solution():
    def maxheapify(self,arr,n,m):
        """
        維護max heap(因為最大值和最後一個值交換位置後會破壞原來的max heap結構)
        """
        left_child = 2*n+1          #左邊child的index
        right_child = 2*n+2                                  #右邊child的index,right_child = 2*n+2  
        max_node = n              #假設當前的max_node為parent
        
        while left_child < m or right_child < m:     #只有left_child存在的情況下才會進行判斷
            if arr[left_child] > arr[right_child]:    #比較leftchild和maxnode大小，若比maxnode大，則把其index更改為leftchild的index
                if arr[left_child] > arr[max_node]:
                    max_node = left_child
                else:
                    break
            else:
                if arr[right_child] > arr[max_node]:
                    max_node = right_child
                else:
                    break
                
        
        if max_node != n:             #如果max_node的index已經發生改變，則交換vaule的位置
            arr[n], arr[max_node] = arr[max_node],arr[n]
            Solution.maxheapify(arr,max_node,m)    #再對新的subtree進行檢查，看是否符合max heap的性質，直到找到最大值為止
        
    def heapbuild(self,arr):
        """
        構建max heap
        """
        m=len(arr)
        i = int(len(arr) / 2 - 1)             #非葉子節點的index。假設list有8個node，則非葉子節點的index為0，1，2，3
        while i >= 0:                  #從最後一個非葉子節點開始
            Solution.maxheapify(arr,i,m)
            i -= 1
        return arr
    
    def heap_sort(self,arr):
        Solution.heapbuild(arr)
        m = len(arr)
        while m >= 0:
            arr[0],arr[len(arr)-1] = arr[len(arr)-1],arr[0]
            m= m-1
            Solution.maxheapify(arr,0,m)
```


```python
arr = [7,10,12,19,30,20,11]
Solution.heap_sort(arr)
arr
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-93-4c70ee881dd6> in <module>()
          1 arr = [7,10,12,19,30,20,11]
    ----> 2 Solution.heap_sort(arr)
          3 arr


    TypeError: heap_sort() missing 1 required positional argument: 'arr'


此處發現呼叫的寫法也有錯，正確寫法還要在Solution后面加()；並且發現輸出的答案已經接近了想要的結果。這裡請教同學之後發現，Solution().heapbuild(arr)的結果不會繼續讓下面的使用，也就是最後輸出的arr還是Solution().heapbuild(arr)的arr。這裡真的花了超級久的時間解決TOT。。。


```python
class Solution():
    def maxheapify(self,arr,n,m):
        """
        維護max heap(因為最大值和最後一個值交換位置後會破壞原來的max heap結構)
        """
        left_child = 2*n+1          #左邊child的index
        right_child = 2*n+2                                  #右邊child的index,right_child = 2*n+2  
        max_node = n              #假設當前的max_node為parent
        
        if left_child<m and arr[left_child]>arr[max_node]:
            max_node = left_child
        if right_child<m and arr[right_child]>arr[max_node]:
            max_node = right_child
                
        
        if max_node != n:             #如果max_node的index已經發生改變，則交換vaule的位置
            arr[n], arr[max_node] = arr[max_node],arr[n]
            Solution().maxheapify(arr,max_node,m)    #再對新的subtree進行檢查，看是否符合max heap的性質，直到找到最大值為止
        
    def heapbuild(self,arr):
        """
        構建max heap
        """
        m=len(arr)
        i = int(len(arr) / 2 - 1)             #非葉子節點的index。假設list有8個node，則非葉子節點的index為0，1，2，3
        while i >= 0:                  #從最後一個非葉子節點開始
            Solution().maxheapify(arr,i,m)
            i -= 1
        Solution().maxheapify(arr,0,m)
        return arr
    
    def heap_sort(self,arr):
        self.arr=arr
        Solution().heapbuild(arr)
        print(arr)
        m = len(arr)
        while m >= 0:
            arr[0],arr[len(arr)-1] = arr[len(arr)-1],arr[0]
            m= m-1
            Solution().maxheapify(arr,0,m)
```


```python
arr = [7,10,12,19,30,20,11]
Solution().heap_sort(arr)
```

    [30, 19, 20, 7, 10, 12, 11]


最後賦值給a，解決問題。


```python
class Solution():
    def maxheapify(self,arr,n,m):
        """
        維護max heap(因為最大值和最後一個值交換位置後會破壞原來的max heap結構)
        """
        left_child = 2*n+1          #左邊child的index
        right_child = 2*n+2                                  #右邊child的index,right_child = 2*n+2  
        max_node = n              #假設當前的max_node為parent
        
        if left_child<m and arr[left_child]>arr[max_node]:
            max_node = left_child
        if right_child<m and arr[right_child]>arr[max_node]:
            max_node = right_child
                
        
        if max_node != n:             #如果max_node的index已經發生改變，則交換vaule的位置
            arr[n], arr[max_node] = arr[max_node],arr[n]
            Solution().maxheapify(arr,max_node,m)    #再對新的subtree進行檢查，看是否符合max heap的性質，直到找到最大值為止
        return arr
        
    def heapbuild(self,arr):
        """
        構建max heap
        """
        m=len(arr)
        i = int(len(arr) / 2 - 1)             #非葉子節點的index。假設list有8個node，則非葉子節點的index為0，1，2，3
        while i >= 0:                  #從最後一個非葉子節點開始
            Solution().maxheapify(arr,i,m)
            i -= 1
        Solution().maxheapify(arr,0,m)
        return arr
    
        
    def heap_sort(self,arr):
        a = Solution().heapbuild(arr)
        m = len(a)
        while m >= 2:
            arr[0],arr[m-1] = arr[m-1],arr[0]
            m= m-1
            Solution().maxheapify(a,0,m)
        return arr
        
```


```python
arr = [7,10,12,19,30,20,11]
Solution().heap_sort(arr)
```




    [7, 10, 11, 12, 19, 20, 30]




```python

```
