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


arr = [7,10,12,19,30,20,11]
Solution().heap_sort(arr)
