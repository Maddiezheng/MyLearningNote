class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head                
        mid = self.findMidNode(head)
        #設置兩個指針，left和right分別指向兩鏈表的最前端。
        left = self.sortList(head)            
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def findMidNode(self, head):
        # 找到中间节点，断开链表，之后再__merge中合并两个链表
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next               #慢指針走一步
            fast = fast.next.next          #快指針走兩步
        p = slow.next                      #當快指針走到最後一步的時候，慢指針就是中點
        slow.next = None                   #此時在中點處斷開，分成兩個鏈表
        return p

    def merge(self, left, right):
        dummy = ListNode(0)               #設置dummy節點。
        tail = dummy
        while left and right:
            if left.val <= right.val:     #比較left和right兩指針處節點的大小
                tail.next = left
                left = left.next          #原left進入合併鏈表，則更新左鏈表的前端節點。
            else:
                tail.next = right
                right = right.next
            tail = tail.next                #不要忘記更新dummy節點，為了方便把比較大小後的節點併入合併鏈表裡，即合併鏈表的指針要指向比較大小後的那個節點。
        
        if left:
            tail.next = left              #只要兩個當中有一個不為空，就把tail.next接上去
        if right:
            tail.next = right
            
        return dummy.next

