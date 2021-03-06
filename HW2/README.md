1. 堆排序(HeapSort)：

它是O（nlogn）排序算法中最慢的，但與合併和快速排序不同，它不需要大量的遞歸或多個數組即可工作。

>*堆排序方法對記錄數較少的文件並不值得提倡，但對n較大的文件還是很有效的。因為其運行時間主要耗費在建初始堆和調整建新堆時進行的反復「篩選」上。 

>*堆排序在最壞的情況下，其時間複雜度也為O(nlogn)，這顯然好於冒泡、簡單選擇和直接插入排序的O(n2)的時間複雜度。相對於快速排序來說，這是堆排序的最大優點。

>*堆排序僅需一個記錄大小的供交換用的輔助存儲空間。


![-w80](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/heapsort流程圖.png)



2. 合併排序(Mergesort)：

對於較大的集合，合併排序比堆排序要快一些，但是由於第二個數組，合併排序需要的內存是堆排序的兩倍。

>*歸並排序對原始序列元素分布情況不敏感，其時間複雜度為O(nlogn)。 

>*歸並排序在計算過程中需要使用一定的輔助空間，用於遞歸和存放結果，因此其空間複雜度為O(n+logn)。 

>*歸並排序中不存在跳躍，只有兩兩比較，因此是一種穩定排序。 


總之，歸並排序是一種比較佔用內存，但效率高，並且穩定的算法。


![-w80](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/mergesort%20flow%20chart.png)


3. 時間空間複雜度比較

               堆排序     歸並排序

       最壞時間 O(nlogn) O(nlogn) 

       最好時間 O(nlogn) O(nlogn) 

       平均時間 O(nlogn) O(nlogn) 

       輔助空間 O(1)    O(n)


4.測試數據

<table><tr><td bgcolor=#cdedf9>測試的平均排序時間：數據為隨機整數，時間單位為s</td></tr></table>

     數據規模    heapsort   mergesort

     1000萬      3.57      1.22

     5000萬      26.54     6.29

     1億         61.31     13.06





參考資料：
https://blog.csdn.net/taotao12312/article/details/69511722
https://blog.csdn.net/chenyukuai6625/article/details/77185426
