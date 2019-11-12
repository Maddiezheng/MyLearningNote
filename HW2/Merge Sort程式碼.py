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

arr=[10,3,6,5,14,8]
Solution().merge_sort(arr)
