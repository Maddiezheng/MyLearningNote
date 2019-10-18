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
[Week1](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Week1(707.Design%20Linked%20List)%202.0.py)

[Week2.1](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Week2(155.Min%20Stack).py)

[Week2.2](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Week2(232.Implement%20Queue%20using%20Stacks).py)

Week3

Week4

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

![](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/linked%20list1.png)
![](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/linked%20list2.png)
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
![](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/stack.png)

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

![](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/queue.png)

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

Week4
====

Insertion Sort(插入排序法)
--------

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

![](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/quicksort.png)


Solution 1
----

Here is [flow chart] which I drew by computer.
(https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Assignment1-flow%20chart(sol1).png)

Solution 2
---

This is my thought process below.

![-w100](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Assignment1-flow%20chart(sol2.1).JPG)

![-w90](https://github.com/Maddiezheng/MyLearningNote/blob/master/Data%20Structures%20and%20Algorithms/Assignment1-flow%20chart(sol2.2).JPG)

 
