### 廣度優先搜索法(Breadth-first Search，BFS)：
#### 是一種圖形搜尋演算法。簡單的說，BFS是從根節點開始，沿著樹的寬度遍歷樹的節點。如果所有節點均被存取，則演算法中止。廣度優先搜尋的實現一般採用open-closed表。用白話講就是「一石激起千層浪」....

廣度優先搜索在進一步遍歷圖中頂點之前，先訪問當前頂點的所有鄰接結點。

#### 執行步驟：
* 首先選擇一個頂點作為起始結點，並將其染成灰色，其餘結點為白色。
*  將起始結點放入隊列中。
* 從隊列首部選出一個頂點，並找出所有與之鄰接的結點，將找到的鄰接結點放入隊列尾部，將已訪問過結點塗成黑色，沒訪問過的結點是白色。如果頂點的顏色是灰色，表示已經發現並且放入了隊列，如果頂點的顏色是白色，表示還沒有發現
* 按照同樣的方法處理隊列中的下一個結點。

基本就是出隊的頂點變成黑色，在隊列里的是灰色，還沒入隊的是白色。





### 深度優先搜尋法(Depth-first Search，DFS)：
#### 是一種用來遍尋一個樹(tree)或圖(graph)的演算法。由樹的根(或圖的某一點當成 根)來開始探尋，先探尋邊(edge)上未搜尋的一節點(vertex or node)，並儘可能深的搜索，直到該節點的所有邊上節點都已探尋；就回溯(backtracking)到前一個節點，重覆探尋未搜尋的節點，直到找到目 的節點或遍尋全部節點。用白話講就是「從起點出發，先把每個方向的點都遍歷完才會改變方向」....
深度優先搜尋法屬於盲目搜索(uninformed search)是利用堆疊(Stack)來處理，通常以遞迴的方式呈現。
#### 執行步驟：

初始條件下所有節點為白色，選擇一個作為起始頂點，按照如下步驟遍歷：
* 選擇起始頂點塗成灰色，表示還未訪問
* 從該頂點的鄰接頂點中選擇一個，繼續這個過程（即再尋找鄰接結點的鄰接結點），一直深入下去，直到一個頂點沒有鄰接結點了，塗黑它，表示訪問過了
* 回溯到這個塗黑頂點的上一層頂點，再找這個上一層頂點的其餘鄰接結點，繼續如上操作，如果所有鄰接結點往下都訪問過了，就把自己塗黑，再回溯到更上一層。
* 上一層繼續做如上操作，知道所有頂點都訪問過。


### BFS的複雜度分析  

* BFS是一種借用佇列來儲存的過程，分層查詢，優先考慮距離出發點近的點。無論是在鄰接表還是鄰接矩陣中儲存，都需要藉助一個輔助佇列，v個頂點均需入隊，最壞的情況下，空間複雜度為O（v）。

* 鄰接表形式儲存時，每個頂點均需搜尋一次，時間複雜度T1=O（v），從一個頂點開始搜尋時，開始搜尋，訪問未被訪問過的節點。最壞的情況下，每個頂點至少訪問一次，每條邊至少訪問1次，這是因為在搜尋的過程中，若某結點向下搜尋時，其子結點都訪問過了，這時候就會回退，故時間復 雜度為O(E)，演算法總的時間復 度為O(|V|+|E|)。

* 鄰接矩陣儲存方式時，查詢每個頂點的鄰接點所需時間為O(V)，即該節點所在的該行該列。又有n個頂點，故算總的時間複雜度為O(|V|^2)。

### DFS的複雜度分析

* DFS演算法是一一個遞迴演算法，需要藉助一個遞迴工作棧，故它的空問複雜度為O(V）。

* 遍歷圖的過程實質上是對每個頂點查詢其鄰接點的過程，其耗費的時間取決於所採用結構。

   鄰接表表示時，查詢所有頂點的鄰接點所需時間為O(E)，訪問頂點的鄰接點所花時間為O（V）,此時，總的時間複雜度為O(V+E)。

   鄰接矩陣表示時，查詢每個頂點的鄰接點所需時間為O(V)，要查詢整個矩陣，故總的時間度為O(V^2)。 

   v為圖的頂點數，E為邊數。

### 各自用途

1.	BFS是用來搜索最短徑路的解是比較合適的，比如求最少步數的解，最少交換次數的解，因為BFS搜索過程中遇到的解一定是離根最近的，所以遇到一個解，一定就是最優解，此時搜索算法可以終止。這個時候不適宜使用DFS，因為DFS搜索到的解不一定是離根最近的，只有全局搜索完畢，才能從所有解中找出離根的最近的解。
2.	DFS是空間效率高，DFS不需要保存搜索過程中的狀態，而BFS在搜索過程中需要保存搜索過的狀態，而且一般情況需要一個隊列來記錄。

3. DFS適合搜索全部的解，因為要搜索全部的解，那麼BFS搜索過程中，遇到離根最近的解，並沒有什麼用，也必須遍歷完整棵搜索樹，DFS搜索也會搜索全部，但是相比DFS不用記錄過多信息，所以搜素全部解的問題，DFS顯然更加合適，一般情況下，DFS也需要高效的剪枝操作。 



## 流程图：



## 參考資料：

https://www.itread01.com/content/1549064200.html

https://www.cnblogs.com/wkfvawl/p/9347828.html

https://www.cnblogs.com/brucekun/p/8503042.html

## 學習歷程：

#### BFS步驟：

* state1為暫存待檢查的值，state2為已經檢查好的隊列；此處再設定一個current來存放可能路徑(只有判斷不在state1和state2中才可以取出存入state1)。
* 把目標值放入state2當中，再在state1中暫存目標值的可能路徑。
* 進入while迴圈：停止檢查的條件是state1裡面沒有東西。利用queue先進先出的概念，把第一個值append到state2裡面，然後把第一個值從state1裡面pop掉。然後進入for迴圈，檢查current存放的值有沒有已經在state1和2當中，沒有的話就塞進state1裡等待被檢查。


#### DFS步驟：

與BFS大同小異，只要更改BFS的部分程式碼使其滿足先進後出(Stack)的要求即可。


```python
from collections import defaultdict 
```


```python
class Graph:
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v):        
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
        """
        :type s: int
        :rtype: list
        """
        p = self.graph[s]             #存放檢索鍵對應的值,例如2:[0,3]，則p為[0,3]
        state1 = []                     #設定state1，暫存點的可能路徑
        state2 = []                    #設定state2來存放最後走的路徑
        state2.append(s)           #把起點加進state2裡面
        state1.append(p)           #把起點的可能路徑存入state1當中
        if p[0] is not in state2:
            state2.append(p[0])      #把起始頂點的下一層頂點append到state2裡面
            state1 = state1[1:]         #
            
            
        
        
        
        
        
        
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
```

發現這樣寫無法做到循環，如果設定state1，p就是數列，state1[0]是數列不是一個元素，所以直接用p來做


```python
class Graph:
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v):        
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
        """
        :type s: int
        :rtype: list
        """
        p = self.graph[s]             #存放檢索鍵對應的值,例如2:[0,3]，則p為[0,3]
        state1 = []                     #設定state1，暫存點的可能路徑
        state2 = []                    #設定state2來存放最後走的路徑
        state2.append(s)           #把起點加進state2裡面
        state1.extend(p)            #把起點的可能路徑存入state1當中
        
        while p is not None:
            state2.append(state1[0])      #把起始頂點的下一層頂點append到state2裡面 
            n=state1[0]
            state1 = state1[1:]         #
            state3=self.graph[n]
            for i in range(len(state3)-1):
                if state3[i] not in state2 and state3[i] not in state1:
                    state1.append(state3[i])
                
        return state2
               
                
            
            
        
        
        
        
        
        
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
```

用p來做。

此處理解啦extend和append的區別。
如果是一個list，append進去還是一個list，extend就是相繼append該list裡面的值。


```python
class Graph:
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v):        
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
        """
        :type s: int
        :rtype: list
        """
        p = self.graph[s]             #存放檢索鍵對應的值,例如2:[0,3]，則p為[0,3]
        state2 = []                    #設定state2來存放最後走的路徑
        state2.append(s)           #把起點加進state2裡面
    
        while p is not None:
            state2.append(p[0])      #把起始頂點的下一層頂點append到state2裡面 
            p = p[1:]         #把暫存數列的第一個值pop出去
            state3=self.graph[n]           #暫存可能路徑，判斷
            for i in range(len(state3)-1):
                if state3[i] not in state2 and state3[i] not in state1:
                    state1.append(state3[i])
                
        return state2
               
                
            
            
        
        
        
        
        
        
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
```


```python
arr=[1]
```


```python
arr.append([1,2,3])
arr
```




    [1, [1, 2, 3]]




```python
from collections import defaultdict 
class Graph:
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v):        
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
        """
        :type s: int
        :rtype: list
        """
        state1 = self.graph[s]             #存放檢索了的鍵對應的值,例如2:[0,3]，則state1為[0,3]
        state2 = []                    #設定state2來存放最後走的路徑
        state2.append(s)           #把起點加進state2裡面
        
        while state1 is not None:
            state3=[]                           #每次循環之前都把state3清空，因為要判斷頂點的可能路徑是否已經存在於state1和state2當中
            p = state1[0]  
            state2.append(p)      #把起始頂點的下一層頂點append到state2裡面      
            state3=self.graph[p]  #先暫存下一個頂點的可能路徑，再判斷是否元素存在在state1和state2裡面
            state1.pop(0)                     #把第一個元素pop出來
            
            for i in range(len(state3)-1):
                if state3[i] not in state2 and state3[i] not in state1:  #如果都不在state1和state2裡面
                    state1.append(state3[i])                 #把可能的路徑就暫存到state1裡面
        return state2
               
        
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
```


```python
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
#g.BFS(2)
print(g.graph)
print(g.BFS(2))
```

    defaultdict(<class 'list'>, {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]})



    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-9-bfd3b4a5936a> in <module>
          8 #g.BFS(2)
          9 print(g.graph)
    ---> 10 print(g.BFS(2))
    

    <ipython-input-8-46dc2db2f5c1> in BFS(self, s)
         22         while state1 is not None:
         23             state3=[]                           #每次循環之前都把state3清空，因為要判斷頂點的可能路徑是否已經存在於state1和state2當中
    ---> 24             p = state1[0]
         25             state2.append(p)      #把起始頂點的下一層頂點append到state2裡面
         26             state3=self.graph[p]  #先暫存下一個頂點的可能路徑，再判斷是否元素存在在state1和state2裡面


    IndexError: list index out of range



```python
print(g.graph)
```

    defaultdict(<class 'list'>, {0: [1, 2], 1: [2], 2: [], 3: [3]})



```python
g.BFS(2)
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-11-6c9d6257770b> in <module>
    ----> 1 g.BFS(2)
    

    <ipython-input-8-46dc2db2f5c1> in BFS(self, s)
         22         while state1 is not None:
         23             state3=[]                           #每次循環之前都把state3清空，因為要判斷頂點的可能路徑是否已經存在於state1和state2當中
    ---> 24             p = state1[0]
         25             state2.append(p)      #把起始頂點的下一層頂點append到state2裡面
         26             state3=self.graph[p]  #先暫存下一個頂點的可能路徑，再判斷是否元素存在在state1和state2裡面


    IndexError: list index out of range


上面的ERROR：IndexError: list index out of range
可是怎麼都找不到錯誤
後來把while的條件改為while state1就能執行了

這裡while state1 is not None和while state1還是有差別的


```python
from collections import defaultdict 
class Graph:
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v):        
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
        """
        :type s: int
        :rtype: list
        """
        p = self.graph[s]             #存放檢索了的鍵對應的值,例如2:[0,3]，則state1為[0,3]
        state1 = [] 
        state2 = []                    #設定state2來存放最後走的路徑
        state2.append(s)           #把起點加進state2裡面
        state1.extend(p)
        
        while state1:
            state3=[]                           #每次循環之前都把state3清空，因為要判斷頂點的可能路徑是否已經存在於state1和state2當中
            state2.append(state1[0])      #把起始頂點的下一層頂點append到state2裡面 
            state3=self.graph[state1[0]]  #先暫存下一個頂點的可能路徑，再判斷是否元素存在在state1和state2裡面
            state1 = state1[1:]                      #把第一個元素pop出來
            
            for i in range(len(state3)-1):
                if state3[i] not in state2 and state3[i] not in state1:  #如果都不在state1和state2裡面
                    state1.append(state3[i])                 #把可能的路徑就暫存到state1裡面
        return state2
               
                
            
            
        
        
        
        
        
        
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
```


```python
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
print(g.BFS(2))
```

    [2, 0, 3, 1]


接下來做DFS的部分：

DFS和BFS的code大同小異，只要在BFS的基礎上更改部分邏輯，滿足先進後出(Stack)的要求即可 -A-


```python
from collections import defaultdict 
class Graph:
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v):        
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
        """
        :type s: int
        :rtype: list
        """
        p = self.graph[s]             #存放檢索了的鍵對應的值,例如2:[0,3]，則state1為[0,3]
        state1 = [] 
        state2 = []                    #設定state2來存放最後走的路徑
        state2.append(s)           #把起點加進state2裡面
        state1.extend(p)
        
        while state1:
            state3=[]  #每次循環之前都把state3清空，因為要判斷頂點的可能路徑是否已經存在於state1和state2當中
            n=state1[0]
            if n not in state2:
                state2.append(state1[0])      #把起始頂點的下一層頂點append到state2裡面 
            state3=self.graph[state1[0]]  #先暫存下一個頂點的可能路徑，再判斷是否元素存在在state1和state2裡面
            state1.pop(0)                     #把第一個元素pop出來
            
            for i in range(len(state3)-1):
                if state3[i] not in state2 and state3[i] not in state1:  #如果都不在state1和state2裡面
                    state1.append(state3[i])                 #把可能的路徑就暫存到state1裡面
        return state2
            
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
        
        n = self.graph[s]           #存放檢索了的鍵對應的值,例如2:[0,3]，則n為[0,3]
        stack1 = []                   #待檢查元素放入的stack1
        stack2 = []                   #最後的路徑
        stack2.append(s)          #把起點放進state2裡面
        stack1.extend(n)           #把起點的鄰近點放入stack1
        
        while stack1:
            stack3 = []#用於判斷可能路徑是否已於stack1和stack2當中
            n=stack1[0]
            if n not in stack2:
                stack2.append(stack1[-1])        #把stack中的最上面pop出來放進stack2裡面
            stack3 = self.graph[stack1[-1]]  #stack3用於暫存stack最上面的元素的可能路徑
            stack1.pop()                          #把stack1最上面pop出來
            
            for x in range(len(stack3)-1):
                if stack3[x] not in stack2 and stack3[x] not in stack1:
                    stack1.append(stack3[x])
        return stack2
        
        
```


```python
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
print(g.BFS(3))
```

    [3]



```python
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
print(g.DFS(2))
print(g.BFS(2))
```

    [2, 3, 0, 1]
    [2, 0, 3, 1]



```python
# g = Graph()
# g.addEdge('A','B')
# g.addEdge('A','D')
# g.addEdge('B','C')
# g.addEdge('B','F')
# g.addEdge('C','E')
# g.addEdge('C','G')
# g.addEdge('G','E')
# g.addEdge('E','B')
# g.addEdge('E','F')
# g.addEdge('F','A')
# g.addEdge('D','F')
# print(g.graph)
# print(g.DFS('B'))
```


```python
g = Graph()
g.addEdge(0,2)
g.addEdge(0,5)
g.addEdge(0,7)
g.addEdge(1,7)
g.addEdge(2,0)
g.addEdge(2,6)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,3)
g.addEdge(4,5)
g.addEdge(4,6)
g.addEdge(4,7)
g.addEdge(5,0)
g.addEdge(5,3)
g.addEdge(5,4)
g.addEdge(6,2)
g.addEdge(6,4)
g.addEdge(7,0)
g.addEdge(7,1)
g.addEdge(7,4)
print(g.graph)
print(g.BFS(2))    #正解：20657431
print(g.DFS(2))
```

    defaultdict(<class 'list'>, {0: [2, 5, 7], 1: [7], 2: [0, 6], 3: [4, 5], 4: [3, 5, 6, 7], 5: [0, 3, 4], 6: [2, 4], 7: [0, 1, 4]})
    [2, 0, 6, 5, 3, 4]
    [2, 6, 0, 5, 3, 4]



```python
state1=[0,6]
state2=[2]
state3=[]
```


```python
測試了別的值，發現會跑出error TAT,只能一步一步看到底是哪裡有問題
```


```python
from collections import defaultdict 
class Graph:
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v):        
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
        """
        :type s: int
        :rtype: list
        """
        p = self.graph[s]             #存放檢索了的鍵對應的值,例如2:[0,3]，則state1為[0,3]
        state1 = [] 
        state2 = []                    #設定state2來存放最後走的路徑
        state2.append(s)           #把起點加進state2裡面
        state1.extend(p)
        
       # while state1:
        state3=[]                           #每次循環之前都把state3清空，因為要判斷頂點的可能路徑是否已經存在於state1和state2當中
        state2.append(state1[0])      #把起始頂點的下一層頂點append到state2裡面 
        state3=self.graph[state1[0]]  #先暫存下一個頂點的可能路徑，再判斷是否元素存在在state1和state2裡面
        state1.pop(0)                     #把第一個元素pop出來
        print(state1)
        print(state2)
        print(state3)
            
        for i in range(len(state3)-1):
            if state3[i] not in state2 and state3[i] not in state1:  #如果都不在state1和state2裡面
                state1.append(state3[i])                 #把可能的路徑就暫存到state1裡面
                print(state1)
        #return state2
            
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
        
        n = self.graph[s]           #存放檢索了的鍵對應的值,例如2:[0,3]，則n為[0,3]
        stack1 = []                   #待檢查元素放入的stack1
        stack2 = []                   #最後的路徑
        stack2.append(s)          #把起點放進state2裡面
        stack1.extend(n)           #把起點的鄰近點放入stack1
        
        while stack1:
            stack3 = []              #用於判斷可能路徑是否已於stack1和stack2當中
            stack2.append(stack1[-1])        #把stack中的最上面pop出來放進stack2裡面
            stack3 = self.graph[stack1[-1]]  #stack3用於暫存stack最上面的元素的可能路徑
            stack1.pop()                          #把stack1最上面pop出來
            
            for x in range(len(stack3)-1):
                if stack3[x] not in stack2 and stack3[x] not in stack1:
                    stack1.append(stack3[x])
        return stack2
        
        
```


      File "<ipython-input-36-ce65847de9d7>", line 37
        print("state1:"state1)
                            ^
    SyntaxError: invalid syntax




```python
找到問題了，在第一次檢查0的可能路徑的時候，7就沒有進入到state1裡面
```


      File "<ipython-input-37-1c8771c98a16>", line 1
        找到問題了，在第一次檢查0的可能路徑的時候，7就沒有進入到state1裡面
                                            ^
    SyntaxError: invalid character in identifier




```python
g = Graph()
g.addEdge(0,2)
g.addEdge(0,5)
g.addEdge(0,7)
g.addEdge(1,7)
g.addEdge(2,0)
g.addEdge(2,6)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,3)
g.addEdge(4,5)
g.addEdge(4,6)
g.addEdge(4,7)
g.addEdge(5,0)
g.addEdge(5,3)
g.addEdge(5,4)
g.addEdge(6,2)
g.addEdge(6,4)
g.addEdge(7,0)
g.addEdge(7,1)
g.addEdge(7,4)
g.BFS(2)
```

    [6]
    [2, 0]
    [2, 5, 7]
    [6, 5]



```python
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(1,0)
g.addEdge(1,4)
g.addEdge(2,0)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(2,6)
g.addEdge(2,7)
g.addEdge(3,0)
g.addEdge(3,7)
g.addEdge(4,1)
g.addEdge(4,2)
g.addEdge(4,5)
g.addEdge(5,2)
g.addEdge(5,4)
g.addEdge(5,8)
g.addEdge(6,2)
g.addEdge(6,7)
g.addEdge(6,8)
g.addEdge(7,2)
g.addEdge(7,3)
g.addEdge(7,6)
g.addEdge(8,5)
g.addEdge(8,6)

g.BFS(0)
```

    [2, 3]
    [0, 1]
    [0, 4]



```python
 g1.AddEdgeList(0, 1);g1.AddEdgeList(0, 2);g1.AddEdgeList(0, 3);
    g1.AddEdgeList(1, 0);g1.AddEdgeList(1, 4);
    g1.AddEdgeList(2, 0);g1.AddEdgeList(2, 4);g1.AddEdgeList(2, 5);g1.AddEdgeList(2, 6);g1.AddEdgeList(2, 7);
    g1.AddEdgeList(3, 0);g1.AddEdgeList(3, 7);
    g1.AddEdgeList(4, 1);g1.AddEdgeList(4, 2);g1.AddEdgeList(4, 5);
    g1.AddEdgeList(5, 2);g1.AddEdgeList(5, 4);g1.AddEdgeList(5, 8);
    g1.AddEdgeList(6, 2);g1.AddEdgeList(6, 7);g1.AddEdgeList(6, 8);
    g1.AddEdgeList(7, 2);g1.AddEdgeList(7, 3);g1.AddEdgeList(7, 6);
    g1.AddEdgeList(8, 5);g1.AddEdgeList(8, 6);

```

    p
    p



```python
from collections import defaultdict 
class Graph:
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v):        
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
        """
        :type s: int
        :rtype: list
        """
        p = self.graph[s]             #存放檢索了的鍵對應的值,例如2:[0,3]，則state1為[0,3]
        queue = [] 
        visited = []                    #設定state2來存放最後走的路徑
        visited.append(s)           #把起點加進state2裡面
        queue.extend(p)
        
        while queue:
            current=[]  #每次循環之前都把state3清空，因為要判斷頂點的可能路徑是否已經存在於state1和state2當中
            n=queue[0]
            
            visited.append(n)      #把起始頂點的下一層頂點append到state2裡面 
            current=self.graph[queue[0]]  #先暫存下一個頂點的可能路徑，再判斷是否元素存在在state1和state2裡面
            
            queue.pop(0)                     #把第一個元素pop出來
            
            for i in range(len(current)):
                if current[i] not in queue and current[i] not in visited:  #如果都不在state1和state2裡面
                    queue.append(current[i])                 #把可能的路徑就暫存到state1裡面
        return visited
            
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
        
        n = self.graph[s]           #存放檢索了的鍵對應的值,例如2:[0,3]，則n為[0,3]
        stack1 =n                  #待檢查元素放入的stack1
        stack2 = [s]                   #最後的路徑
        #stack2.append(s)          #把起點放進state2裡面
        #stack1.extend(n)           #把起點的鄰近點放入stack1
        
        while stack1:
            stack3 = []#用於判斷可能路徑是否已於stack1和stack2當中
            stack2.append(stack1[-1])        #把stack中的最上面pop出來放進stack2裡面
            stack3 = self.graph[stack1[-1]]  #stack3用於暫存stack最上面的元素的可能路徑
            stack1.pop()                          #把stack1最上面pop出來
            
            for x in range(len(stack3)):
                if stack3[x] not in stack2 and stack3[x] not in stack1:
                    stack1.append(stack3[x])
        return stack2
        
        
```


```python
g = Graph()
g.addEdge(0,2)
g.addEdge(0,5)
g.addEdge(0,7)
g.addEdge(1,7)
g.addEdge(2,0)
g.addEdge(2,6)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,3)
g.addEdge(4,5)
g.addEdge(4,6)
g.addEdge(4,7)
g.addEdge(5,0)
g.addEdge(5,3)
g.addEdge(5,4)
g.addEdge(6,2)
g.addEdge(6,4)
g.addEdge(7,0)
g.addEdge(7,1)
g.addEdge(7,4)
print(g.graph)
print(g.BFS(2))    #正解：20657431
print(g.DFS(2))
```

    defaultdict(<class 'list'>, {0: [2, 5, 7], 1: [7], 2: [0, 6], 3: [4, 5], 4: [3, 5, 6, 7], 5: [0, 3, 4], 6: [2, 4], 7: [0, 1, 4]})
    [2, 0, 6, 5, 7, 4, 3, 1]
    [2, 6, 4, 7, 1, 5, 3, 0]



```python
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
print(g.DFS(2))
print(g.BFS(2))
```

    [2, 3, 0, 1]
    [2]


檢查之後發現是range的範圍寫錯了，不應該長度減去1。

如果list裡面只有1個值的時候，這裡的range就是[0,0)，所以for迴圈不會執行。


```python
from collections import defaultdict 
class Graph:
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v):        
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
        """
        :type s: int
        :rtype: list
        """
        p = self.graph[s]             #存放檢索了的鍵對應的值,例如2:[0,3]，則state1為[0,3]
        state1 = [] 
        state2 = []                    #設定state2來存放最後走的路徑
        state2.append(s)           #把起點加進state2裡面
        state1.extend(p)
        
        while state1:
            current=[]  #每次循環之前都把state3清空，因為要判斷頂點的可能路徑是否已經存在於state1和state2當中
            n=state1[0]
            
            state2.append(n)      #把起始頂點的下一層頂點append到state2裡面 
            current=self.graph[state1[0]]  #先暫存下一個頂點的可能路徑，再判斷是否元素存在在state1和state2裡面
            
            state1.pop(0)                     #把第一個元素pop出來
            
            for i in range(len(current)):
                if current[i] not in state1 and current[i] not in state2:  #如果都不在state1和state2裡面
                    state1.append(current[i])                 #把可能的路徑就暫存到state1裡面
        return state2
            
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
        
        n = self.graph[s]           #存放檢索了的鍵對應的值,例如2:[0,3]，則n為[0,3]
        stack1 = []                   #待檢查元素放入的stack1
        stack2 = []                   #最後的路徑
        stack2.append(s)          #把起點放進state2裡面
        stack1.extend(n)           #把起點的鄰近點放入stack1
        
        while stack1:
            stack3 = []#用於判斷可能路徑是否已於stack1和stack2當中
            n=stack1[0]
            if n not in stack2:
                stack2.append(stack1[-1])        #把stack中的最上面pop出來放進stack2裡面
            stack3 = self.graph[stack1[-1]]  #stack3用於暫存stack最上面的元素的可能路徑
            stack1.pop()                          #把stack1最上面pop出來
            
            for x in range(len(stack3)):
                if stack3[x] not in stack2 and stack3[x] not in stack1:
                    stack1.append(stack3[x])
        return stack2
        
```


```python
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
print(g.DFS(2))
print(g.BFS(2))
```

    [2, 3, 0, 1]
    [2, 0, 3, 1]



```python
g = Graph()
g.addEdge(0,2)
g.addEdge(0,5)
g.addEdge(0,7)
g.addEdge(1,7)
g.addEdge(2,0)
g.addEdge(2,6)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,3)
g.addEdge(4,5)
g.addEdge(4,6)
g.addEdge(4,7)
g.addEdge(5,0)
g.addEdge(5,3)
g.addEdge(5,4)
g.addEdge(6,2)
g.addEdge(6,4)
g.addEdge(7,0)
g.addEdge(7,1)
g.addEdge(7,4)
print(g.graph)
print(g.BFS(2))    #正解：20657431
print(g.DFS(2))
```

    defaultdict(<class 'list'>, {0: [2, 5, 7], 1: [7], 2: [0, 6], 3: [4, 5], 4: [3, 5, 6, 7], 5: [0, 3, 4], 6: [2, 4], 7: [0, 1, 4]})
    [2, 0, 6, 5, 7, 4, 3, 1]
    [2, 6, 4, 7, 1, 5, 3, 0]


這樣子程式碼就完全正確了！


```python

```
