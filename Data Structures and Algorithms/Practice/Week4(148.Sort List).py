# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def findMid(self, head):
        # 尋找中間節點，然後斷開鏈表，再使用merge合併兩個鏈表
        slow = head   #使用快慢指針
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next               #慢指針始終走一步
            fast = fast.next.next          #快指針始終走兩步
        n = slow.next                      #n指向中間節點的下一個節點
        slow.next = None                   #此時在中點處斷開，分成兩個鏈表
        return n                           ##

    def merge(self, left, right):
        dummy = ListNode(0)               #設置虛擬的dummy節點
        tail = dummy                      #dummy用於記錄merge鏈表當前的最後一個位置
        while left and right:             #left和right分別為兩鏈表的表頭
            if left.val <= right.val:     
                tail.next = left          #若左邊鏈表的表頭比右邊小，則併入已排序的鏈表
                left = left.next          #原left進入合併鏈表，則更新左鏈表的前端節點。
            else:
                tail.next = right
                right = right.next
            tail = tail.next              #不要忘記更新dummy節點，為了方便把比較大小後的節點併入合併鏈表裡，即合併鏈表的指針要指向比較大小後的那個節點。
        
        if left == None:                  ##
            tail.next = right
        if right == None:
            tail.next = left
        return dummy.next
    
    def sortList(self, head):
        if not head or not head.next:
            return head                
        mid = self.findMid(head)
        #設置兩個指針，left和right分別指向兩鏈表的最前端。
        left = self.sortList(head)            
        right = self.sortList(mid)       ##
        return self.merge(left, right)

