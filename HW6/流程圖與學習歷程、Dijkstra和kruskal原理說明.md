## Dijkstra原理（Shortest path）：

1.介紹

* Dijkstra算法是典型最短路徑算法，用於計算一個節點到其他節點的最短路徑。
* 它的主要特點是以起始點為中心向外層層擴展(廣度優先搜索思想)，直到擴展到終點為止。
* Dijkstra算法能得出最短路徑的最優解，但由於它遍歷計算的節點很多，所以效率低。

2.原理

* 首先，引入一個輔助向量D，它的每個分量 D[i]保存當前所找到的從起始點v到其它每個頂點vi的長度；一個保存已經找到了最短路徑的頂點的集合：T
* D的初始狀態為: 若從v到vi有弧，則D[i]為弧上的權值否則置D[i]為∞; T的初始狀態為{v}
* 從D數組選擇最小值，則該值就是源點v到該值對應的頂點的最短路徑，並且把該點加入到T中，OK，此時完成一個頂點。
* 然後，我們需要看看新加入的頂點是否可以到達其他頂點並且看看通過該頂點到達其他點的路徑長度是否比源點直接到達短，如果是，那麼就替換這些頂點D中的值
* 從D中找出最小值，重復上述動作，直到T中包含了圖的所有頂點


3.流程圖

## Kruskal原理（Minimum Spanning tree）：

1.介紹

* 生成樹的概念 ：在一個連通圖中取出這個圖的全部頂點和一部分邊形成的一個無環圖就是這個連通圖的生成樹。在圖中，任意取出圖中的一條邊都使得這個圖中沒有環路，也就形成了一棵樹。
* 最小生成樹：在一個連通圖的所有生成樹中，邊的權重之和最小的那棵樹稱為最小生成樹

2.原理

* 記Graph中有v個頂點，e個邊

* 新建圖Graph_new，Graph_new中擁有原圖中相同的e個頂點，但沒有邊
* 將原圖Graph中所有e個邊按權值從小到大排序
* 循環：從權值最小的邊開始遍歷每條邊 直至圖Graph中所有的節點都在同一個連通分量中
                If 這條邊連接的兩個節點於圖Graph_new中不在同一個連通分量中
                                         添加這條邊到圖Graph_new中


3.流程圖

#參考資料


```python
#https://blog.csdn.net/John_xyz/article/details/79357873
#https://www.cnblogs.com/DWVictor/p/10282696.html
#https://blog.csdn.net/tianjindong0804/article/details/86573765
#https://baike.baidu.com/item/最短路径/6334920?fr=aladdin
#https://blog.csdn.net/yalishadaa/article/details/55827681
#https://baike.baidu.com/item/最小生成树/5223845?fr=aladdin
```

## Dijkstra的部分：

因為會用到各個path比較大小，找到最小值，所以這邊設定了一個function叫FinMin


```python
from collections import defaultdict 

class node:
    def __init__(self,v,n,w):
        self.v=v
        self

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] #self.graph的第一個位置是第一行
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    
    def FindMin(self,arr):
        Min_stack=[]
        for i in range(len(arr)):             #把第一個不為0的值當成最小值
            if arr[i] !=0:
                Min_stack.append(b[i])
                break
            i+=1
        for i in range(len(arr)):            #比較除零以外的每個值，最小值加入min_stack的後面
            if b[i] < Min_stack[-1] and b[i] != 0:
                Min_stack.append(b[i])
        return Min_stack[-1]
            
        
    def addEdge(self,u,v,w): 
  

    def Dijkstra(self, s): 
        visited=[]   #存放已經檢視過的點
        weight=[]   #存放點的weight
        cover=[]    #覆蓋掉原weight的list
        
        visited.append(s)
        weight=self.graph[s]     #存放起點的weight，起點的index就是本身
        min_index=arr.index(self.FindMin(weight))   #取出和起點路徑最短(最小值)的index
        visited.append(min_index)                         
        cover=self.graph_matrix[min_index]           #最小值的weight
        for i in range(1,len(cover)):    #排除 
            if i not in visited:
                if cover[i]>weight[i]:
                    weight[i]=cover[i]
                    
            self.FindMin(weight)
        
        
        
            
        
        
        
        
    
    def Kruskal(self):
     
    
```


      File "<ipython-input-6-6461de3e9bc1>", line 32
        def Dijkstra(self, s):
          ^
    IndentationError: expected an indented block



發現尋找最小值還需要加入排除已經檢查過的點，所以添加了「if i not in visited」的條件


```python
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] #self.graph的第一個位置是第一行
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    
    def FindMin(self,arr):
        Min_stack=[]
        for i in range(len(arr)):             #把第一個不為0的值當成最小值
            if i not in visited:
                if arr[i] !=0:
                    Min_stack.append(arr[i])
                    break
           
        for i in range(len(arr)):            #比較除零以外的每個值，最小值加入min_stack的後面
            if i not in visited:
                if arr[i] < Min_stack[-1] and arr[i] != 0:
                    Min_stack.append(arr[i])
        return Min_stack[-1]
    
    def Dijkstra(self, s): 
        visited=[]   #存放已經檢視過的點
        weight=[]   #存放點的weight
        cover=[]    #覆蓋掉原weight的list
        
        visited.append(s)
        weight=self.graph[s]     #存放起點的weight，起點的index就是本身
        min_index=arr.index(self.FindMin(weight))   #取出和起點路徑最短(最小值)的index
        visited.append(min_index)                         
        cover=self.graph_matrix[min_index]           #最小值的weight
        if i not in visited :    #訪問過的點和 不檢查
            cover+weight[min_index]
                
    
    def new_weight(self,weight):
        min_index=arr.index(self.FindMin(weight))   #取出和起點路徑最短(最小值)的index
        visited.append(min_index)                         
        cover=self.graph_matrix[min_index]           #最小值的weight
        for i in range(len(cover)):    #排除 
            if i not in visited:
                if weight[i] == 0 and cover[i]>weight[i]:
                    weight[i]=cover[i]
                    
            return self.new_weight(weight)
        
    def addEdge(self,u,v,w): 
  


        
        
        
            
        
        
        
        
    
    #def Kruskal(self):
     
    
```


      File "<ipython-input-8-384065da0664>", line 63
        
        ^
    SyntaxError: unexpected EOF while parsing



最新更正：：：


```python
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] #self.graph的第一個位置是第一行
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    
    def FindMin(self,arr):
        Min_stack=[]
        for i in range(len(arr)):             #把第一個不為0的值當成最小值
            if i not in visited:
                if arr[i] !=0:
                    Min_stack.append(arr[i])
                    break
           
        for i in range(len(arr)):            #比較除零以外的每個值，最小值加入min_stack的後面
            if i not in visited:
                if arr[i] < Min_stack[-1] and arr[i] != 0:
                    Min_stack.append(arr[i])
        return Min_stack[-1]
    
    def Dijkstra(self, s): 
        short_path=dict()
        p=str(s)      #把s變為字串
        short_path[p]=0       #把起點到起點的值為0
        len_graph=list()
        
        visited=[]   #存放已經檢視過的點
        weight=[]   #存放點的weight
        cover=[]    #覆蓋掉原weight的list
        
        visited.append(s)
        weight=self.graph[s]     #存放起點的weight，起點的index就是本身
        min_index=weight.index(self.FindMin(weight))   #取出和起點路徑最短(最小值)的index
        visited.append(min_index) 
        cover=self.graph_matrix[min_index]
        short_path[str(min_index)]=weight[min_index] 
        
        while len(visited)<len(weight):
            for i in range(len(cover)):
                if i in visited:
                    cover[i]==0
                else:
                    if cover[i] != 0:
                        cover_i=cover[i]+weight[min_index]    #cover[i]的值，後面要比大小
                        if weight[i]==0:
                            cover[i]=cover_i
                        else:
                            if weight[i]<cover_i:
                                cover[i]=weight[i]
            min_index=weight.index(self.FinMin(cover))
            visited.append(min_index)
            short_path[str(min_index)]=weight[min_index]
            
                        
                        
                    
                    
                    
                
        
    #def addEdge(self,u,v,w): 
  


        
        
        
            
        
        
        
        
    
    #def Kruskal(self):
     
    
```


```python
g = Graph(9)
g.graph=[[0,4,0,0,0,0,0,8,0],
        [4,0,8,0,0,0,0,11,0],
        [0,8,0,7,0,4,0,0,2],
        [0,0,7,0,9,14,0,0,2],
        [0,0,0,9,0,10,0,0,0],
        [0,0,4,14,10,0,2,0,0],
        [0,0,0,0,0,2,0,1,6],
        [8,11,0,0,0,0,1,0,7],
        [0,0,2,0,0,0,6,7,0]]
```


```python
g.Dijkstra(0)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-11-c69afaf9b43b> in <module>
    ----> 1 g.Dijkstra(0)
    

    <ipython-input-9-8456b32daaee> in Dijkstra(self, s)
         33         visited.append(s)
         34         weight=self.graph[s]     #存放起點的weight，起點的index就是本身
    ---> 35         min_index=weight.index(self.FindMin(weight))   #取出和起點路徑最短(最小值)的index
         36         visited.append(min_index)
         37         cover=self.graph_matrix[min_index]


    <ipython-input-9-8456b32daaee> in FindMin(self, arr)
         10         Min_stack=[]
         11         for i in range(len(arr)):             #把第一個不為0的值當成最小值
    ---> 12             if i not in visited:
         13                 if arr[i] !=0:
         14                     Min_stack.append(arr[i])


    NameError: name 'visited' is not defined


邏輯還是有錯誤，重新更改一下。
FinMin直接寫到function內部裡，不再設定新的



```python
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] #self.graph的第一個位置是第一行
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    
    def Dijkstra(self, s): 
        short_path=dict()
        p=str(s)      #把s變為字串
        short_path[p]=0       #把起點到起點的值為0
        
        visited=[]   #存放已經檢視過的點
        weight=[]   #存放路徑的weight
        cover=[0]*len(self.graph[s])    #覆蓋掉原weight的list
        cover[s]=1
        visited.append(s)
        weight=self.graph[s]     #存放起點的weight，起點的index就是本身
        
        while len(visited)<len(weight):
            for i in range(len(cover)):
                if cover==0 and weight[i]!=0:
                    x=i
                    break
            for i in range(len(cover)):
                    if cover[i] == 0 and weight[i] != 0 and weight[x]>weight[i]:
                        x=i
            visited.append(x)
            short_path[str(x)]=weight[x]
            cover[x]=1
            weight1=[]
            for i in range(0,len(weight)):
                if self.graph[x][i]!=0:
                    weight1.append(short_path[str(x)]+self.graph[x][i])
                else:weight.append(0)
            
            for i in range(0,len(weight)):
                if weight[i]==0 or(weight[i]!=0 and weight1!=0 and weight1[i]<weight[i]):
                    weight[i]=weight1[i]
            for i in range(0,len(weight)-1):
                if cover[i]!=0:
                    weight[i]=0
        return short_path
                
                        
                    
                    
                    
                
        
    #def addEdge(self,u,v,w): 
  


        
        
        
            
        
        
        
        
    
    #def Kruskal(self):
     
    
```


```python
g = Graph(9)
g.graph=[[0,4,0,0,0,0,0,8,0],
        [4,0,8,0,0,0,0,11,0],
        [0,8,0,7,0,4,0,0,2],
        [0,0,7,0,9,14,0,0,2],
        [0,0,0,9,0,10,0,0,0],
        [0,0,4,14,10,0,2,0,0],
        [0,0,0,0,0,2,0,1,6],
        [8,11,0,0,0,0,1,0,7],
        [0,0,2,0,0,0,6,7,0]]
```


```python
g.Dijkstra(0)
```


    ---------------------------------------------------------------------------

    UnboundLocalError                         Traceback (most recent call last)

    <ipython-input-15-c69afaf9b43b> in <module>
    ----> 1 g.Dijkstra(0)
    

    <ipython-input-13-4e420aa46e30> in Dijkstra(self, s)
         25                     break
         26             for i in range(len(cover)):
    ---> 27                     if cover[i] == 0 and weight[i] != 0 and weight[x]>weight[i]:
         28                         x=i
         29             visited.append(x)


    UnboundLocalError: local variable 'x' referenced before assignment



```python
a = [0,4,0,0,0,0,0,8,0]
```


```python
for i in range(a):    
    for n in a:
        if a[i] != 0 and n != 0:
            if n < a[i]:
                Min = n
i += 1
            
                
```




    0




```python
Min_stack=[]
b=[0,0,0,8,4]
for i in range(1,len(b)):
    if b[i] !=0:
        Min_stack.append(b[i])
        break
    i+=1

for i in range(1,len(b)):
    if b[i] < Min_stack[-1] and b[i] != 0:
        Min_stack.append(b[i])
    

        

```




    [8, 4]




```python
Min_stack
```




    [4]




```python
class Graph(): 
    def FindMin(self,arr):
        Min_stack=[]
        for i in range(len(arr)):             #把第一個不為0的值當成最小值
            if arr[i] !=0:
                Min_stack.append(b[i])
                break
            i+=1
        for i in range(len(arr)):            #比較除零以外的每個值，最小值加入min_stack的後面
            if b[i] < Min_stack[-1] and b[i] != 0:
                Min_stack.append(b[i])
        return Min_stack[-1]
```


```python
b=[0,8,0,7,0,3,0,0,2]
Graph().FindMin(b)
```




    2




```python
arr.index(Graph().FindMin(b))
```




    8




```python
visited=[2,8,5]
```


```python
weight=[0,8,0,7,0,4,6,7,2]
cover=[0,0,4,14,10,0,2,0,0]
for i in range(1,len(cover)):    #排除 
    if i not in visited:
        if weight[i] == 0 and cover[i]>weight[i]:
            weight[i]=cover[i]
            
```


```python
weight
```




    [0, 8, 0, 7, 10, 4, 6, 7, 2]




```python
class Graph(): 
    def FindMin(self,arr):
        visited=[2,8]
        Min_stack=[]
        for i in range(len(arr)):             #把第一個不為0的值當成最小值
            if i not in visited:
                if arr[i] !=0:
                    Min_stack.append(arr[i])
                    break
                
        for i in range(len(arr)):            #比較除零以外的每個值，最小值加入min_stack的後面
            if i not in visited:
                if arr[i] != 0 and arr[i] < Min_stack[-1] :
                    Min_stack.append(arr[i])
        return Min_stack[-1]
```


```python
weight=[0,8,0,7,0,4,6,7,2]
#cover=[0,0,2,0,0,0,6,7,0]
Graph().FindMin(weight)
```




    4




```python
class Graph(): 
    def FindMin(self,arr):
        visited=[2]
        Min_stack=[]
        for i in range(len(arr)):             #把第一個不為0的值當成最小值
            if i not in visited:
                if arr[i] !=0:
                    Min_stack.append(arr[i])
                    break
        print(Min_stack)
```


```python
weight=[0,8,0,7,0,4,0,0,2]
#cover=[0,0,2,0,0,0,6,7,0]
Graph().FindMin(weight)
```

    [8]



```python

```


```python
Min_stack=[]
arr=[3,2,1]
if arr[1]<Min_stack[-1]:
    print("True")
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-33-64cf2e86b8f9> in <module>
          1 Min_stack=[]
          2 arr=[3,2,1]
    ----> 3 if arr[1]<Min_stack[-1]:
          4     print("True")


    IndexError: list index out of range



```python
visited=[]
if 3 not in visited:
    print("True")
```

    True



```python
ppgraph=[]
ppgraph[1][1]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-14-ce832bcd95de> in <module>
          1 ppgraph=[]
    ----> 2 ppgraph[1][1]
    

    IndexError: list index out of range



```python
cover=[0,0,8,0,0,0,0,11,0]
min_index=1
weight=[0,4,0,0,0,0,0,8,0]
```


```python
cover_i=cover[2]+weight[min_index] 
cover_i
```




    12




```python
cover=[4,0,8,0,0,0,0,11,0]
min_index=1
weight=[0,4,0,0,0,0,0,8,0]
visited=[0,1]
```


```python
for i in range(len(cover)):
    if i in visited:
        cover[i]=0
    else:
        if cover[i] != 0:
            cover_i=cover[i]+weight[min_index]    #cover[i]的值，後面要比大小
            if weight[i]==0:
                cover[i]=cover_i
            else:
                if weight[i]<cover_i:
                    cover[i]=weight[i]
                        
```


```python
cover
```




    [0, 0, 12, 0, 0, 0, 0, 8, 0]




```python
class Node():
    def __init__(self,u,v,w):
        self.u=u
        self.v=v
        self.w=w
        
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices    #
        self.graph = [] #self.graph的第一個位置是第一行
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    
    def Dijkstra(self, s): 
        short_path=dict()
        p=str(s)      #把s變為字串
        short_path[p]=0       #把起點到起點的值為0
        
        visited=[]   #存放已經檢視過的點
        weight=[]   #存放路徑的weight
        cover=[0]*len(self.graph[s])    #覆蓋掉原weight的list
        cover[s]=1
        visited.append(s)
        weight=self.graph[s]     #存放起點的weight，起點的index就是本身
        
        while len(visited)<len(weight):
            x=0
            for i in range(len(cover)):
                if cover[i]==0 and weight[i]!=0:
                    x=i
                    break
                
            for a in range(len(cover)):
                    if cover[a] == 0 and weight[a] != 0 and weight[x]>weight[a]:
                        x=a
            visited.append(x)
            short_path[str(x)]=weight[x]
            cover[x]=1
            weight1=[]
            for i in range(0,len(weight)):
                if self.graph[x][i]!=0:
                    weight1.append(short_path[str(x)]+self.graph[x][i])
                else:weight1.append(0)

            for i in range(0,len(weight)):
                if weight[i]==0 or(weight[i]!=0 and weight1[i]!=0 and weight1[i]<weight[i]):
                    weight[i]=weight1[i]
            for i in range(0,len(weight)-1):
                if cover[i]!=0:
                    weight[i]=0
                    
        arr=short_path
        short_path=dict()
        for i in range(0,len(arr)):
            short_path[str(i)]=arr[str(i)]
            
        return short_path
          
```


```python
g = Graph(9)
g.graph=[[0,4,0,0,0,0,0,8,0],
        [4,0,8,0,0,0,0,11,0],
        [0,8,0,7,0,4,0,0,2],
        [0,0,7,0,9,14,0,0,2],
        [0,0,0,9,0,10,0,0,0],
        [0,0,4,14,10,0,2,0,0],
        [0,0,0,0,0,2,0,1,6],
        [8,11,0,0,0,0,1,0,7],
        [0,0,2,0,0,0,6,7,0]]
```


```python
g.Dijkstra(0)
```




    {'0': 0, '1': 4, '2': 12, '3': 19, '4': 21, '5': 11, '6': 9, '7': 8, '8': 14}



## Kruskal的部分：

這邊要先設定No的function，uvw代表起點，終點和weight


```python
class Node():
    def __init__(self,u,v,w):
        self.u=u
        self.v=v
        self.w=w
        
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices    #
        self.graph = [] #self.graph的第一個位置是第一行
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    
    def Dijkstra(self, s): 
        short_path=dict()
        p=str(s)      #把s變為字串
        short_path[p]=0       #把起點到起點的值為0
        
        visited=[]   #存放已經檢視過的點
        weight=[]   #存放路徑的weight
        cover=[0]*len(self.graph[s])    #覆蓋掉原weight的list
        cover[s]=1
        visited.append(s)
        weight=self.graph[s]     #存放起點的weight，起點的index就是本身
        
        while len(visited)<len(weight):
            x=0
            for i in range(len(cover)):
                if cover[i]==0 and weight[i]!=0:
                    x=i
                    break
                
            for a in range(len(cover)):
                    if cover[a] == 0 and weight[a] != 0 and weight[x]>weight[a]:
                        x=a
            visited.append(x)
            short_path[str(x)]=weight[x]
            cover[x]=1
            weight1=[]
            for i in range(0,len(weight)):
                if self.graph[x][i]!=0:
                    weight1.append(short_path[str(x)]+self.graph[x][i])
                else:weight1.append(0)

            for i in range(0,len(weight)):
                if weight[i]==0 or(weight[i]!=0 and weight1[i]!=0 and weight1[i]<weight[i]):
                    weight[i]=weight1[i]
            for i in range(0,len(weight)-1):
                if cover[i]!=0:
                    weight[i]=0
                    
        arr=short_path
        short_path=dict()
        for i in range(0,len(arr)):
            short_path[str(i)]=arr[str(i)]
            
        return short_path
```

創建addEdge用以構建符合條件的關係圖


```python
    def addEdge(self,u,v,w): 
        n=Node(u,v,w)
        self.graph.append(n)      
```

因為要從小排到大，所以要有一個排序的function，這邊使用了之前寫HW2時寫的Merge sort，並對程式碼略做了更動。


```python
    def MergeSingle(self,left_arr,right_arr):
            
            i = 0          #left array的index
            j = 0          #right array的index
            a=[]           #設定的空list
            mid=len(left_arr)       #left array的最大index
            end=len(right_arr)     #right array的最大index
            while i<mid and j<end:     #在i和j都在index範圍裡的時候比較
                if left_arr[i].w<=right_arr[j].w:
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
        arr1=self.merge_sort(arr[:mid])  #遞迴左半邊的array
        arr2=self.merge_sort(arr[mid:]) #遞迴左半邊的array
        return self.MergeSingle(arr1,arr2)#單趟merge
```

最後再針對Kruskal的function內部進行程式碼的撰寫


```python
class Node():
    def __init__(self,u,v,w):
        self.u=u
        self.v=v
        self.w=w
        
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices    #
        self.graph = [] #self.graph的第一個位置是第一行
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    
    def Dijkstra(self, s): 
        short_path=dict()
        p=str(s)      #把s變為字串
        short_path[p]=0       #把起點到起點的值為0
        
        visited=[]   #存放已經檢視過的點
        weight=[]   #存放路徑的weight
        cover=[0]*len(self.graph[s])    #覆蓋掉原weight的list
        cover[s]=1
        visited.append(s)
        weight=self.graph[s]     #存放起點的weight，起點的index就是本身
        
        while len(visited)<len(weight):
            x=0
            for i in range(len(cover)):
                if cover[i]==0 and weight[i]!=0:
                    x=i
                    break
                
            for a in range(len(cover)):
                    if cover[a] == 0 and weight[a] != 0 and weight[x]>weight[a]:
                        x=a
            visited.append(x)
            short_path[str(x)]=weight[x]
            cover[x]=1
            weight1=[]
            for i in range(0,len(weight)):
                if self.graph[x][i]!=0:
                    weight1.append(short_path[str(x)]+self.graph[x][i])
                else:weight1.append(0)

            for i in range(0,len(weight)):
                if weight[i]==0 or(weight[i]!=0 and weight1[i]!=0 and weight1[i]<weight[i]):
                    weight[i]=weight1[i]
            for i in range(0,len(weight)-1):
                if cover[i]!=0:
                    weight[i]=0
                    
        arr=short_path
        short_path=dict()
        for i in range(0,len(arr)):
            short_path[str(i)]=arr[str(i)]
            
        return short_path
          
                
                        
    def addEdge(self,u,v,w): 
        n=Node(u,v,w)
        self.graph.append(n)      
    
    def Kruskal(self):
        MST=dict()
        arr=self.merge_sort(self.graph)
        a=[]
        for i in range(len(self.graph)):
            if self.graph[i].u not in a:
                a.append(self.graph[i].u)
            if self.graph[i].v not in a:
                a.append(self.graph[i].v)
        b=a
        a=[]
        for i in range(len(b)):
            a.append([b[i]])
        for i in range(len(arr)):
            for n in range(len(a)):
                if arr[i].u in a[n]:
                    one=n
                if arr[i].v in a[n]:
                    two=n
            if one==two:continue
            else:
                a[one].extend(a[two])
                a.remove(a[two])
                MST[str(arr[i].u)+'-'+str(arr[i].v)]=arr[i].w
        return MST
        
        
        
    def MergeSingle(self,left_arr,right_arr):
            
            i = 0          #left array的index
            j = 0          #right array的index
            a=[]           #設定的空list
            mid=len(left_arr)       #left array的最大index
            end=len(right_arr)     #right array的最大index
            while i<mid and j<end:     #在i和j都在index範圍裡的時候比較
                if left_arr[i].w<=right_arr[j].w:
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
        arr1=self.merge_sort(arr[:mid])  #遞迴左半邊的array
        arr2=self.merge_sort(arr[mid:]) #遞迴左半邊的array
        return self.MergeSingle(arr1,arr2)#單趟merge
```


```python
g = Graph(4)
g.addEdge(0,1,10)
g.addEdge(0,2,6)
g.addEdge(0,3,5)
g.addEdge(1,3,15)
g.addEdge(2,3,4)
g.Kruskal()
```




    {'2-3': 4, '0-3': 5, '0-1': 10}




```python

```
