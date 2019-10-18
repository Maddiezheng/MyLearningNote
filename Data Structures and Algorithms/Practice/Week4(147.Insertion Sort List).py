# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        取出未排序list的第一個node：cur
        從list已經遍歷排序好的list中，找到cur適當的位置並插入
        """
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)    #設置虛擬node永遠指向head，val不重要可隨便設定
        dummy.next = head      
        pre = head             #pre始終指向排序好的list的最後一個node，head會隨遍歷而移動
        cur = head.next        #cur始終指向未排序好的list的第一個node
        while cur:
            tail = cur.next
            pre.next = tail    #取出cur，使pre與tail連接
            
            p = dummy
            while p.next and p.next.val < cur.val: #找到插入的位置
                p = p.next     #把拿出的node和已經排序好的list內node一一比較
                
            cur.next = p.next  #把cur插入dummy與dummy.next之間，用cur的pointer指向原dummy.next，則原dummy.next向後移
            p.next = cur       #再將dummy與cur做連接
            cur = tail         #cur被抽出進行排序後，現在的cur則變為原cur的下一個tail
            
            if p == pre:       #若剛剛插入的到了已排序list的末端
                pre = pre.next #則更新pre
        return dummy.next
