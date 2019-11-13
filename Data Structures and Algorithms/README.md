About the course
====
Course Information
-----------------------
* Course Title: DATA STRUCTURES AND ALGORITHMS
* Instructor：TSAI, YUN-CHENG
* Semester: 2019-1
* Credits: 3

Objectives
-----
> * Understand the data structure: such as arrays, links, trees, and graphs.
> * Ability to use a language to implement basic data structures.
> * Understand the simple algorithm that corresponds to the primary data structure.
> * Ability to analyze simple algorithms to assess their pros and cons.
> * This course is based on the Python but is not limited to Python.
> * Students are free to use familiar tools.

Contents
=========
[Week1](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Practice/Week1(707.Design%20Linked%20List)%202.0.py):Linked List

[Week2.1](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Practice/Week2(155.Min%20Stack).py):Stack

[Week2.2](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Practice/Week2(232.Implement%20Queue%20using%20Stacks).py):Queue

[Week3](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Practice/Week3(645.Set%20Mismatch).py):Set

[Week4.1](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Practice/Week4(147.Insertion%20Sort%20List).py):Insertion Sort

[Week4.2](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Practice/Week4(148.Sort%20List).py):Sort List

[Assignment1](https://nbviewer.jupyter.org/github/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Assignment/Assignment1-QuickSort.ipynb):Quick Sort

[Week5]:Heap

What's "leetcode" ?
----------
> “LeetCode is the best platform to help you enhance your skills, expand your knowledge and prepare for technical interviews.” (From leetcode.com) 

> Essentially, leetcode is a site with a variety of tools focused on programming interview questions. One of the main parts of the site is dedicated to a list of problems, each tagged with a different computer science term that it is supposed to be based on. These tags range from “dynamic programming” to “binary tree.” Some of the tags are company names, “Google” or “Dropbox” or “Twitter,” indicating that they are questions asked at the named company. Many of these questions are locked behind a paywall.
> Another part of the site is a series of coding competitions.

Week1
=======
> Leetcode: 707. Design Linked List

Linked List
------
Linked list is a common data structure that uses `Node` to record, represent, store data, and use the `pointer` in each node to point to the next node, thereby using multiple nodes. Connected together to form a Linked list, and `NULL` to represent the end of the Linked list.

![](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/linked%20list1.png)
![](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/linked%20list2.png)
Week2
=====
>Leetcode: 155.Min Stack & 232.Implement Queue using Stacks 

Stack
-----
Stack is a data structure with "Last-In-First-Out" (can be imagined as a container for loading data), "The latest entry into Stack" will be "first taken out", and "early into Stack" will be "It was taken out at the latest."

For a general Stack, there are several functions for processing data structures:
* `Push(data)`: Put the data into the Stack.
  * Put the book in the box. 
* `Pop`: Remove the "topmost" data from the Stack.
  * Take out the book at the top of the box.
* `Top`: Returning the "topmost" information does not affect the data structure itself.
  * Confirm which book is currently at the "top" of the box.
* `IsEmpty`: Confirm whether there is data in the Stack and does not affect the data structure itself.
  * Confirm that there are books in the box.
* `getSize`: Returns the number of data in the Stack, without affecting the data structure itself.
  * Record how many books are currently in the box.
![](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/stack.png)

For the above example, the Stack is empty at the beginning:
  
* When `Push(6)`, Put 6 on the Stack. And use a variable called `top` to record the top of the Stack data, here is 6.
* When `Push(3)` 、 `Push(7)`, put 3, 7 on the Stack. And update the `top` to make it record 7.
* When `Pop()`, the "topmost" data in the Stack (7) to remove, so there are 6 and 3 left in the stack.And update the `top` record 3
* When `Push(14)`, `Push(8)`, put 14 and 8 on the Stack. And update `top` to make it record 8
* At any of the above stages, as long as the Stack has data, using the function `Top()` will return the data recorded by the variable `top`.
* At any of the above stages, `IsEmpty()` can be used to determine if there is any data stored in the Stack.
* At any of the above stages, using `getSize()` will return the number of data in the Stack.

Queue
----
Queue is a data structure with "First-In-First-Out". Just like a team that queues to buy a ticket, it can be regarded as a Queue. The person who enters the team first can leave the team first, go to the ticket window to buy a ticket, and then the person who arrives, You need to wait for the people in front of the team to buy the ticket before you can buy it.

Like the generally recognized queuing team, Queue also has the following characteristics:

* The team has points in front and in back.
* To enter the team, you must enter from the back.
* To leave the team, you must be away from the front.

![](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/queue.png)

As shown in the above figure, it can be judged from the front (front of the team) and back (behind the team) that the order of entering the team should be 23, 1, 3, 35.

For a general Queue, there are several functions for processing data structures:
* `Push(data)`: puts the data from the "back" of the Queue into the Queue and updates it to a new back.
  * Adding information to the Queue is also called enqueue.
* `Pop`: Remove the data pointed to by the front from the Queue and update the front.
  * Deleting data from the Queue is also known as dequeue.
* `getFront`: Returns the data pointed to by the front.
* `getBack`: Returns the data pointed to by back.
* `IsEmpty`: Confirm if there is any data in the Queue.
* `getSize`: Returns the number of data in the Queue.

Week3
====
> Leetcode: 645.Set Mismatch

Week4
====
>Leetcode: 147.Insertion Sort List & 148.Sort List

Insertion Sort(插入排序法)
--------

Sort List
----
This is my [flow chart](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/sort%20list.png) I draw.
![-w80](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/sort%20list.png)


The question requires that the time complexity(時間複雜度) is O(nlogn) and space complexity(空間複雜度) is O(1). According to the time complexity, we naturally think of the dichotomy(二分法), which associates with the merge order(歸併排序).

There are `two steps` to achieve the merge sorting of linked lists by recursion(遞歸).

* `Cut step`(分割環節): Find the `midpoint` of the current linked list and disconnect the linked list from the midpoint.

   * Using the `fast`, `slow` double-pointer method, an odd number(奇數) of nodes finds the midpoint, and an even number(偶數) of nodes finds the node to the left of the center.
   * After finding the midpoint `slow`, execute `slow.next = None` to cut the list.
   * For recursive splitting(遞歸分割), enter the left end head of the current list and the next node tmp of the center node slow (because the linked list is cut from slow).
   * Cut Recursive termination condition(cut遞歸終止條件):  When head.next == None, it means that there is only one node, and it returns directly to this node.
   
* `Merge step`(合併環節): Combine two sorted linked lists into one sorted linked list.

   * Use Double pointer method to merge, create ListNode dummy as header.
   * Set two pointers `left`, `right` respectively point to the head of the two linked list, compare the node value of the two pointers, add the merged list header from small to large, and the pointer alternates until the two linked lists are added.
   * Returns ListNode dummy as the next node of the header dummy.next




Assignment 1: Quick Sort
=====

Quicksort is an ecient inplace sorting algorithm, which usually performs about two to three times faster than merge sort and heapsort when implemented well. Quicksort is a comparison sort, meaning that it can sort items of any type for which a
less-than relation is dened. Inecient implementations, it is Quicksort is an ecient inplace sorting algorithm, which usually not a stable sort.

Quicksort is an ecient inplace sorting algorithm, which Quicksort on average takes O(nlog(n)) comparisons to sort n items. In the worst case, it makes O(n) comparisons, though this behavior is very rare.

How Quicksort works?
-----
Quicksort is a divide and conquer algorithm. Like all divide and conquer algorithms, it rst divides a large array into two smaller subarrays and then recursively sort the sub-arrays. Basically, three steps are involved in whole process –

* ***Pivot selection***: Pick an element, called a pivot, from the array (usually the leftmost or the rightmost element of the partition).
* ***Partitioning***: Reorder the array so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it (equal values can go either way). After this partitioning, the pivot is in its nal position.while all elements with values greater than the pivot
* ***Recur***: Recursively apply the above steps to the sub-array of elements with smaller values than pivot and separately to the sub-array of elements with greater values than pivot.

The base case of the recursion is arrays of size 1, which never need to be sorted. 
Below diagram shows how at each step of the quicksort algorithm we choose leftmost element as pivot, partition the array across pivot and recur on two sub-arrays we get after partition process.

![](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/quicksort.png)


Solution 1
----

Here is [flow chart](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/Assignment1-flow%20chart(sol1).png) which I drew by computer.
![-w80](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/Assignment1-flow%20chart(sol1).png)

Solution 2
---

This is my thought process below.

![-w80](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/Assignment1-flow%20chart(sol2.1).JPG)

![-w80](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/Assignment1-flow%20chart(sol2.2).JPG)

Assignment 2: Heap sort & Merge Sort
====

Heap sort
---

The structure of the heap can be divided into `Max Heap` and `Min heap`, which is a complete binary tree, and heap sort is a sorting according to this data structure design of the heap.

* Max heap: Each node(parent node) is bigger than its left child and right child.
    * arr(i) > arr(2i+1)
    * arr(i) > arr(2i+2)
* Min heap: Each node(parent node) is smaller than its left child and right child.
    * arr(i) < arr(2i+1)
    * arr(i) < arr(2i+2)

![-w30](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/maxheap.png)
![-w30](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/minheap.png)

if the index of certain node is i, then:
* index of parent node: (i-1)/2
* index of left child: 2*i+1
* index of right child: 2*i+2

Max Heapify:
![-w30](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/maxheapify1.png)
![-w30](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/maxheapify2.png)
![-30](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/maxheapify3.png)

Heap Sort:
![-w30](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/heapsort1.png)
![-w30](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/heapsort2.png)
![-w30](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/heapsort3.png)
![-w30](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/heapsort4.png)
The steps of heap sort
---

* Step 1:First construct the max heap.The maximum value of the entire array is the top of the heap structure.
```python
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
```

* Stap 2:Max heapify.The number at the top is exchanged with the number at the end. At this time, the number at the end is the maximum value, and the number of remaining arrays to be sorted is n-1.
```python
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
```

* Step 3:Reconstruct the remaining array(length: n-1) into a max heap, and then exchange the number of tops with the index n-1 of number. After repeated execution, an ordered array can be obtained.
```python
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
```
>Reference: http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html


Merge Sort
---
Merge Sort is an efficient sorting method. It is divided into two parts: `divide` and `merge`.
`Divide` is to split a bunch of unordered numbers into a single, which is convenient for merging.
`Merge` is to combine the divided numbers which are already sorted.

![-w30](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/mergesort%20flow%20chart.png)

one time merge:

```python
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
```

divide the array,and recursive `Solution().merge_sort` and `Solution().MergeSingle` 

```python
    def merge_sort(self,arr):
        if len(arr)<=1:         #如果array長度不大於1，則直接回傳，默認已經排序
            return arr
        
        
        mid = len(arr)//2  #這裡的//是省略小數，方便取中點
        arr1=Solution().merge_sort(arr[:mid])  #遞迴左半邊的array
        arr2=Solution().merge_sort(arr[mid:]) #遞迴左半邊的array
        return Solution().MergeSingle(arr1,arr2)#單趟merge
```
 
