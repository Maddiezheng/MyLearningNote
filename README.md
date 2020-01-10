About me
=====
:neckbeard:: Maddie Zheng

:round_pushpin:: China

:house:: Taipei,Taiwan

:school:: Dept. of Big data management & Dept. of German Language and Literature,Soochow University





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

My review of the course
========

To be honest, this course is the most painful course in my college career.

Changing from department of  German language to dept. of big data management has been a big challenge for me.

In this half year, there are joys and pains, but what I have gained is the most memorable memories in my learning career.

This semester, I increased my programming skills (Python).

In the past six months, I have used python to write algorithms. I have a deeper understanding of some grammatical structures of python, and my own logical ability has improved a lot.

Have a deeper grasp of algorithms.

I started from the Linked list at first. I didn’t know anything about the algorithm at first. I found it very difficult to write Leetcode or homework. I had to go to the Internet to query related information and learn the logical thinking of others to complete the problem.... But after one semester of training and 6 assignments, I found that I can gradually get out of the process of finding information from the third assignment, because I already have the initial thinking ability and the ability to write algorithm with my own logic. And the speed of writing homework has also gradually increased. It will take 30 to 40 hours at first, and can be completed in 10 to 20 hours later.

Have a clearer plan for the future.

My instructor is a great teacher, and she has brought us a lot of resources with her rich experience. So now I gradually consciously develop my ability to prepare for the future.


Contents
=========
Week1:Moon Festival

Week2:First class

[Week3_Leetcode](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Practice/Week1(707.Design%20Linked%20List)%202.0.py):Linked List

[Week4.1_Leetcode](https://github.com/Maddiezheng/MyLearningNote/blob/master/Leetcode/155%23_Min%20Stack_06123901.py):Stack

[Week4.2_Leetcode](https://github.com/Maddiezheng/MyLearningNote/blob/master/Leetcode/232%23_Implement%20Queue%20using%20Stacks_06123901.py):Queue

[Week5_Leetcode](https://github.com/Maddiezheng/MyLearningNote/blob/master/Leetcode/645%23_Set%20Mismatch_06123901.py):Set

[Week6.1_Leetcode](https://github.com/Maddiezheng/MyLearningNote/blob/master/Leetcode/147%23_Insertion%20Sort%20List_06123901.py):Insertion Sort

[Week6.2_Leetcode](https://github.com/Maddiezheng/MyLearningNote/blob/master/Leetcode/148%23_Sort%20List_06123901.py):Sort List

[Assignment1](https://github.com/Maddiezheng/MyLearningNote/blob/master/HW1): Quick Sort

[Assignment2](https://github.com/Maddiezheng/MyLearningNote/tree/master/HW2): Heap Sort & Merge Sort

[Assignment3](https://github.com/Maddiezheng/MyLearningNote/blob/master/HW3): Binary search tree

[Assignment4](https://github.com/Maddiezheng/MyLearningNote/blob/master/HW4): Hash table

[Assignment5](https://github.com/Maddiezheng/MyLearningNote/blob/master/HW5): BFS & DFS

[Assignment6](https://github.com/Maddiezheng/MyLearningNote/tree/master/HW6): Dijkstra & Kruskal

[CS50](https://github.com/Maddiezheng/MyLearningNote/tree/master/CS50):Harvard University

:city_sunset:[Pictures](https://github.com/Maddiezheng/MyLearningNote/tree/master/Data%20Structures%20and%20Algorithms):file “data structure and algorithm”

What's "leetcode" ?
----------
> “LeetCode is the best platform to help you enhance your skills, expand your knowledge and prepare for technical interviews.” (From leetcode.com) 

> Essentially, leetcode is a site with a variety of tools focused on programming interview questions. One of the main parts of the site is dedicated to a list of problems, each tagged with a different computer science term that it is supposed to be based on. These tags range from “dynamic programming” to “binary tree.” Some of the tags are company names, “Google” or “Dropbox” or “Twitter,” indicating that they are questions asked at the named company. Many of these questions are locked behind a paywall.
> Another part of the site is a series of coding competitions.


Week3
=======
> Leetcode: 707. Design Linked List

> 🔗Course PPT：https://docs.google.com/presentation/d/e/2PACX-1vTB218-EdUZ5jpNz6Uv4TOZQc37Y281v128_aRcWC6EhkTQs5bS8fh7yysmcuzb9R2QPN6_PDshFWL_/pub?start=false&loop=false&delayms=3000&slide=id.p

Linked List
------
Linked list is a common data structure that uses `Node` to record, represent, store data, and use the `pointer` in each node to point to the next node, thereby using multiple nodes. Connected together to form a Linked list, and `NULL` to represent the end of the Linked list.

![](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/linked%20list1.png)
![](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/linked%20list2.png)
Week4
=====
> Leetcode: 155.Min Stack & 232.Implement Queue using Stacks 

> 🔗Course PPT：https://docs.google.com/presentation/d/e/2PACX-1vQ1hb79im0vqpApCttGnXAFRT8SqH9HQP0b_oyVRCV8SVyiHLkHJjidYGAfxkvq468QMumFIDdTeiB-/pub?start=false&loop=false&delayms=3000&slide=id.p

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

Week5
====
> Leetcode: 645.Set Mismatch

> 🔗Course PPT：https://docs.google.com/presentation/d/e/2PACX-1vT6BvB7aI9oLgyum8tdIgGVr8kabqtwo8KZV3ayzKKQqGkpAnvrjT3JabWu-Hms9kUaDILyCU8-Qqhl/pub?start=false&loop=false&delayms=3000&slide=id.p


Week6
====
> Leetcode: 147.Insertion Sort List & 148.Sort List

> 🔗Course PPT：https://docs.google.com/presentation/d/e/2PACX-1vQOTMDM-5-OUaGfnLUOFVgefFwSVRplSwnbicp0CXOQrB5H8RM_1Aq8o_4JxHlncEmhjvqk3tzcoB7s/pub?start=false&loop=false&delayms=3000&slide=id.p

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



Week7:Quick Sort(Assignment1)
====

> 🔗Course PPT：https://docs.google.com/presentation/d/e/2PACX-1vSqz8sTxT4xyjgiz-htLvZd7FZ_5ZzgKf60pFEoNLU5S77JxrsGJ2vd15CdxlfLtT3g2aizHP-Ebk9b/pub?start=false&loop=false&delayms=3000&slide=id.p

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

Week8:Heap sort & Merge Sort(Assignment 2)
====

Heap sort
---
> 🔗Course PPT：https://docs.google.com/presentation/d/e/2PACX-1vRAGwnUvg6BcXoML5u9f4gO6YKcz0vXf7bDnPho_S7mG5D0SBR78djt91RKUPMxqNfkVIcu3l5WCXPh/pub?start=false&loop=false&delayms=3000&slide=id.p

The structure of the heap can be divided into `Max Heap` and `Min heap`, which is a complete binary tree, and heap sort is a sorting according to this data structure design of the heap.

* Max heap: Each node(parent node) is bigger than its left child and right child.
    * arr(i) > arr(2i+1)
    * arr(i) > arr(2i+2)
* Min heap: Each node(parent node) is smaller than its left child and right child.
    * arr(i) < arr(2i+1)
    * arr(i) < arr(2i+2)

![-w110](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/maxheap.png)
![-w110](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/minheap.png)

if the index of certain node is i, then:
* index of parent node: (i-1)/2
* index of left child: 2*i+1
* index of right child: 2*i+2

Max Heapify:

![-w110](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/maxheapify1.png)
![-w110](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/maxheapify2.png)
![-110](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/maxheapify3.png)

Heap Sort:

![-w110](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/heapsort1.png)
![-w110](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/heapsort2.png)
![-w110](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/heapsort3.png)
![-w110](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/heapsort4.png)
>Reference: http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html


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



Merge Sort
---
> 🔗Course PPT：https://docs.google.com/presentation/d/e/2PACX-1vToxkEzc1H1RT5MI9G941KQFBC7GO_Efn95wTqXLEdr3LDBSNcQb-M46IOC-_RzZih6IBEwwy3rWQuE/pub?start=false&loop=false&delayms=3000&slide=id.p

Merge Sort is an efficient sorting method. It is divided into two parts: `divide` and `merge`.
`Divide` is to split a bunch of unordered numbers into a single, which is convenient for merging.
`Merge` is to combine the divided numbers which are already sorted.

![-w110](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Picture/mergesort%20flow%20chart.png)
>Reference: http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html




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

Week 9
====
Binary tree
---

> 🔗Course PPT：https://docs.google.com/presentation/d/e/2PACX-1vSC3P8sGElP48mJTjqT309470SmTFBwJXWsU9hTX2hg5tVpiG4yC703qA7ibPep-Qakmm2Mw_F-ScZh/pub?start=false&loop=false&delayms=3000&slide=id.p

Week 10:Binary Search Tree(Assignment3)
===
> 🔗Course PPT：https://docs.google.com/presentation/d/e/2PACX-1vQgUh73yvSdxAvMH50DHWJ5lsCX8-daMxtoltU9rYW7xCmqYz2A1wOv0Vcx_F9KO5ZUvZBv3IF1TjGi/pub?start=false&loop=false&delayms=3000&slide=id.p

Tree
---

A tree is a data structure. It consists of a set of hierarchical relationships consisting of n(n>=0) finite nodes. It is called a "tree" because it looks like an upside down tree, that is, its roots are facing up, and the leaves are facing down. It has the following characteristics:

* Each node has zero or more `child nodes`.
* A node without a parent node is called `Root Node`.
* Each non-root node has one and only one `parent node`.
* In addition to the root node, each child node can be divided into multiple disjoint `subtrees`.


*`Degree of node`: The number of subtrees owned by the node. The degree of node c in the figure is 2.
*`Leaf`: The node with zero degree, D, E, and F are all leaf nodes. 
*`Degree of the tree`: The maximum degree of the node in the tree. The degree of the node c in the figure is at most 2, so the degree of the tree is 2.

*`level`: The level of the root node is 1, and the level of the remaining nodes is equal to the level of the parent node of the node plus 1. 
*`Height of the tree`: The maximum level of nodes in the tree. The height of the tree in the figure is 3. 
*`Unordered tree`: If the order between the subtrees of the nodes in the tree is not important, the locations can be swapped. *`Ordered tree`: If the order between the subtrees of the nodes in the tree is important, the locations can not be swapped. *`Forest`: 0 or more disjoint trees. Adding a root to the forest, the forest becomes a tree; when the root is deleted, the tree becomes a forest.

Binary Tree
---
A tree whose elements have at most 2 children is called a Binary Tree.That means every node can have maximum 2 children.


Binary Search Tree
===
Search tree is a data structure that can be inserted, searched, deleted, etc., and can be used as a dictionary or priority queue. 

The binary search tree is the simplest search tree.Each parent node has two child nodes (child nodes may be empty). The key value of its left subtree <= the key value of the root node, the key value of the right subtree>= the key value of the root node.

For each node in the tree:
* If its left subtree exists, the value of each node in its left subtree is not greater than the node value.
* If its right subtree exists, the value of each node in its right subtree is not less than the node value.

Week 11
====
> 🔗Course PPT：https://docs.google.com/presentation/d/e/2PACX-1vRxyJRARq0BNuGJq_o2cUHIXBWrRSZrAOyXOSt9qCTSjQtyp8XqFq3VuNn3gCt3sXenOZmWLqIjcyFs/pub?start=false&loop=false&delayms=3000&slide=id.p

Red Black tree
---
In addition to the requirements imposed on a binary search tree the following must be satisfied by a red–black tree:

* Each node is either red or black.

* The root is black. This rule is sometimes omitted. Since the root can always be changed from red to black, but not necessarily vice versa, this rule has little effect on analysis.

* All leaves (NIL) are black.

* If a node is red, then both its children are black.

* Every path from a given node to any of its descendant NIL nodes contains the same number of black nodes.

Week 12：Hash table(Assignment4)
====
> 🔗Course PPT：https://docs.google.com/presentation/d/e/2PACX-1vT1HO9Nl475k2bR0l1x8_Tr4V5Wzx0BEqp9bpmHckvj8kTeJehhYVlOJUDVPhLQm6kjGCJ_sLMSBUw5/pub?start=false&loop=false&delayms=3000&slide=id.p

What's Hash table
----
It is a data structure that is directly accessed according to a key value. That is, it accesses records by mapping key values to a location in the table to speed up lookups. This mapping function is called a hash function, and the array holding the records is called a hash table. If the key of number pair p is k and the hash function is f, then ideally, the position of p in the hash table is f (k).

Hash collision: In the ideal case, different keys will be converted into different index values, but in some cases we need to deal with the case where multiple keys are hashed to the same index value.


Hash table access process
----

① First use the hash function to convert the searched key into an array index.

Computes its hashcode based on key. Assuming that the number of buckets is n, this key-value pair should be placed in the (hashcode% n) bucket.

② If a hash collision occurs, use the zipper method or linear detection method to deal with the hash collision.

If there are already key-value pairs in the bucket, that is, different keywords get the same hash address, then the zipper method or the open addressing method (linear detection method) is used to resolve the conflict.

Week 13
====
> 🔗Course PPT：https://docs.google.com/presentation/d/e/2PACX-1vSYJYXUXvGAeTZ5fknxj_-EPm3zxgy4ITdImrXzy63Y-iZgs8uwVNmOaZlnx9fUNzsbo8kphvMTa0c4/pub?start=false&loop=false&delayms=3000&slide=id.p

Breadth-First Search（BFS）
-----

Is a graph search algorithm. Simply put, BFS starts from the root node and traverses the nodes of the tree along the width of the tree. If all nodes are accessed, the algorithm is aborted. The implementation of breadth-first search generally uses open-closed tables. 

Breadth-first search accesses all adjacent nodes of the current vertex before further traversing the vertices in the graph.

Steps:

* First select a vertex as the starting node and dye it gray, and the remaining nodes are white.

* Put the starting node in the queue.

*Select a vertex from the head of the queue, and find all the nodes that are adjacent to it. Put the found adjacent nodes into the tail of the queue. Paint the visited nodes in black, and the unvisited nodes are white. If the color of the vertex is gray, it means it has been found and put into the queue. If the color of the vertex is white, it means it hasn't been found yet.

* Do the same for the next node in the queue.

Basically, the apex of the team becomes black, the ones in the queue are gray, and the ones that have not joined the team are white.



Week 14:BFS & DFS(Assignment5)
====
> 🔗Course PPT：https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.p


Depth-First Search(DFS)
----
It is an algorithm used to traverse a tree or graph. Start the search by the root of the tree (or a certain point of the graph as the root), first search for a node (vertex or node) on the edge that is not searched, and search as deep as possible until all nodes on the edge of the node Has been searched; backtracking to the previous node, repeatedly searching for unsearched nodes until the destination node is found or all nodes are searched. In vernacular, it is "from the starting point, the points in each direction must be traversed before changing the direction" ...

Depth-first search belongs to uninformed search, which is processed using stacks, and is usually presented in a recursive manner.

Steps:

In the initial condition, all nodes are white, select one as the starting vertex, and traverse as follows:

* Select the starting vertex in gray to indicate that it has not been visited

* Select one of the adjacent vertices of the vertex, continue this process (ie, find the adjacent nodes of the adjacent nodes), and continue to deepen until a vertex has no adjacent nodes, blackened it, indicating that it has been visited
Go back to the top vertex of this blackened vertex, and then find the remaining adjacent nodes of this previous vertex. Continue to operate as above. If all adjacent nodes have been visited downwards, blacken yourself and go back to the top. layer.

* The previous layer continues to do the same operation, knowing that all vertices have been visited.


Week 15:Minimum Spanning Tree（Kruskal）
====
> 🔗Course PPT：https://docs.google.com/presentation/d/e/2PACX-1vTorNDEyhYA4ZAt5jEqOmFs2cQiUAYvkTp-R0DOn9B3c1MuUecV-a1wNakFIrJxA6AoUFGzbl3OQBIJ/pub?start=false&loop=false&delayms=3000&slide=id.p

Spanning Tree Concept
----

An acyclic graph formed by taking out all the vertices and some edges of a graph in a connected graph is the spanning tree of this connected graph. In the figure, arbitrarily taking out an edge in the figure makes no loops in the figure, and a tree is formed.
Minimum Spanning Tree: Of all the spanning trees of a connected graph, the tree with the smallest sum of edges' weights is called the minimum spanning tree

Principle
------
* Remember that there are v vertices and e edges in Graph.

* Create a new graph Graph_new. Graph_new has the same e vertices in the original graph, but no edges.

* Sort all e edges in the original graph from small to large by weight

* Loop: traverse each edge from the edge with the smallest weight until all nodes in the graph Graph are in the same connected component. If the two nodes connected by this edge are in the graph Graph_new, do not add this edge to the graph connected graph_new. in



Week 16:Shortest Path（Dijkstra）
====
> 🔗Course PPT：https://docs.google.com/presentation/d/e/2PACX-1vTgHO5AkHJS6iN6bnnBMMdHv6E4rabnrC0KwyTRfjad8Ab3IQjbnGvZuQOjDC9t7nKqeroiwcuasJrI/pub?start=false&loop=false&delayms=3000&slide=id.p

Introduction
----

* Dijkstra algorithm is a typical shortest path algorithm used to calculate the shortest path from one node to other nodes.

* Dijkstra algorithm is a typical shortest path algorithm used to calculate the shortest path from one node to other nodes.
* Its main feature is to expand to the outer layer with the starting point as the center (the breadth-first search idea) until it reaches the end point.
* Dijkstra's algorithm can get the optimal solution of the shortest path, but because it has many nodes to traverse the calculation, it is inefficient.

Principle
----


* First, an auxiliary vector D is introduced. Each component D [i] holds the currently found length from the starting point v to each of the other vertices vi; a set of vertices that have found the shortest path: T

* The initial state of D is: if there is an arc from v to vi, then D [i] is the weight on the arc; otherwise, D [i] is set to ∞; the initial state of T is {v}

* Select the minimum value from the D array, the value is the shortest path from the source point v to the vertex corresponding to the value, and add this point to T, OK, and a vertex is completed at this time.

* Then, we need to see if the newly added vertex can reach other vertices and see if the length of the path to other points through the vertex is shorter than the direct arrival of the source point, if so, then replace the values in these vertices D

* Find the minimum value from D and repeat the above action until T contains all the vertices of the graph

Week 17:Dijkstra & Kruskal(Assignment6)
====



Week 18
===
No class








