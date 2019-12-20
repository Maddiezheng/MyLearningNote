from collections import defaultdict 
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 
 
    def addEdge(self,u,v):        
        self.graph[u].append(v) 
  
    def BFS(self, s): 
      
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



#https://super9.space/archives/1562

#https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
