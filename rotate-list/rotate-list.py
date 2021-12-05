# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        n=0
        while cur:
            n+=1
            cur=cur.next
        if n == 0 :
            return None
        k=k%n
        answer_head = answer = ListNode(0)
        i = 0
        cur = head
        temp_head = temp = ListNode(0)
        while i < n:
            v = cur.val
            cur = cur.next
            if i < n-k :
                temp.next = ListNode(v)
                temp=temp.next
            else :
                answer.next = ListNode(v)
                answer = answer.next 
            i+=1
        answer.next = temp_head.next
        return (answer_head.next)
            
        
        