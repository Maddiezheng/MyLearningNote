# 147.Insertion Sort List
🔗https://leetcode.com/problems/insertion-sort-list/

Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

* Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

### Example 1:

Input: 4->2->1->3

Output: 1->2->3->4

### Example 2:

Input: -1->5->3->4->0

Output: -1->0->3->4->5



# 148. Sort List
🔗https://leetcode.com/problems/sort-list/

Sort a linked list in O(n log n) time using constant space complexity.

### Example 1:

Input: 4->2->1->3

Output: 1->2->3->4

### Example 2:

Input: -1->5->3->4->0

Output: -1->0->3->4->5


# 155. Min Stack
🔗https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

* push(x) -- Push element x onto stack.
* pop() -- Removes the element on top of the stack.
* top() -- Get the top element.
* getMin() -- Retrieve the minimum element in the stack.
 

### Example:

MinStack minStack = new MinStack();

minStack.push(-2);

minStack.push(0);

minStack.push(-3);

minStack.getMin();   --> Returns -3.

minStack.pop();

minStack.top();      --> Returns 0.

minStack.getMin();   --> Returns -2.



# 232. Implement Queue using Stacks
🔗https://leetcode.com/problems/implement-queue-using-stacks/

Implement the following operations of a queue using stacks.

* push(x) -- Push element x to the back of queue.
* pop() -- Removes the element from in front of queue.
* peek() -- Get the front element.
* empty() -- Return whether the queue is empty.

### Example:

MyQueue queue = new MyQueue();

queue.push(1);

queue.push(2);  

queue.peek();  // returns 1

queue.pop();   // returns 1

queue.empty(); // returns false

### Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).



# 645. Set Mismatch
🔗https://leetcode.com/problems/set-mismatch/

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

### Example 1:

Input: nums = [1,2,2,4]

Output: [2,3]

### Note:

The given array size will in the range [2, 10000].

The given array's numbers won't have any order.



# 705. Design HashSet
🔗https://leetcode.com/problems/design-hashset/

Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

* add(value): Insert a value into the HashSet. 
* contains(value) : Return whether the value exists in the HashSet or not.
* remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

### Example:

MyHashSet hashSet = new MyHashSet();

hashSet.add(1);      

hashSet.add(2);     

hashSet.contains(1);    // returns true

hashSet.contains(3);    // returns false (not found)

hashSet.add(2);          

hashSet.contains(2);    // returns true

hashSet.remove(2);          

hashSet.contains(2);    // returns false (already removed)

### Note:

All values will be in the range of [0, 1000000].

The number of operations will be in the range of [1, 10000].

Please do not use the built-in HashSet library.
