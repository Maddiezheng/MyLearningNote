from collections import defaultdict 

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


#測資
#g = Graph(9)
#g.graph=[[0,4,0,0,0,0,0,8,0],
        #[4,0,8,0,0,0,0,11,0],
        #[0,8,0,7,0,4,0,0,2],
        #[0,0,7,0,9,14,0,0,2],
        #[0,0,0,9,0,10,0,0,0],
        #[0,0,4,14,10,0,2,0,0],
        #[0,0,0,0,0,2,0,1,6],
        #[8,11,0,0,0,0,1,0,7],
        #[0,0,2,0,0,0,6,7,0]]
#g.Dijkstra(0)

#g = Graph(4)
#g.addEdge(0,1,10)
#g.addEdge(0,2,6)
#g.addEdge(0,3,5)
#g.addEdge(1,3,15)
#g.addEdge(2,3,4)
#g.Kruskal()

#https://blog.csdn.net/sm20170867238/article/details/89988982
#https://zh.wikipedia.org/wiki/戴克斯特拉算法
#http://www.csie.ntnu.edu.tw/~u91029/Path.html
#https://ithelp.ithome.com.tw/articles/10209593
#http://dreamisadream97.pixnet.net/blog/post/168577620-dijkstra演算法
#http://www.csie.ntnu.edu.tw/~u91029/SpanningTree.html
#https://www.itread01.com/content/1550409678.html
#http://www.csd.nutn.edu.tw/Algorithm/Ch03.pdf

