# Quick Sort
Quick Sort是一種「把大問題分成小問題處理」的Divide and Conquer方法，概念如下：

在數列中任意挑選一個數，稱為pivot，然後調整數列，使得「所有在pivot左邊的數，都比pivot還小」，而「在pivot右邊的數都比pivot大」。
接著，將所有在pivot左邊的數視為「新的數列」，所有在pivot右邊的數視為「另一個新的數列」，「分別」重複上述步驟(選pivot、調整數列)，直到分不出「新的數列」為止。


## 介紹：Partition
Partition的功能就是把數列「區分」成「小於pivot」與「大於pivot」兩半。



## 時間複雜度
Quicksort 是一個非常熱門且應用廣泛的排序法，相對簡單的實作就可達到O(nlogn) 的平均時間複雜度。 
雖然最差時間複雜度與bubble sort 同為O(n2)，但這種情形非常少見。 
簡單的最佳化實作下，Quicksort 僅需O(logn) 的額外儲存空間，比它的競爭對手mergesort 來得節省。

![-w80](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/quicksort.png)

參考資料：
http://alrightchiu.github.io/SecondRound/comparison-sort-quick-sortkuai-su-pai-xu-fa.html
