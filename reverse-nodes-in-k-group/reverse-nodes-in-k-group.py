# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseChunk(head):
            res = ListNode()
            prev, cur = head,head.next#chunk, chunk.next
            temp = ListNode(prev.val)
            new_head = None
            while True:
                new_head = ListNode(cur.val)
                new_head.next = temp
                temp = new_head
                if not cur.next:
                    break
                prev = cur
                cur = cur.next
            res.next = temp
            return res.next
        
        if k == 1:
            return head
        res_h = res_cur = ListNode()
        cur = head
        chunknum = 0
        while cur :
            
            chunk_h = chunk_cur = ListNode()
            while chunknum < k and cur:
                chunknum+=1
                chunk_cur.next = ListNode(cur.val)
                cur=cur.next
                chunk_cur = chunk_cur.next
            
            if chunknum == k:
                res_cur.next = reverseChunk(chunk_h.next)
            else :
                res_cur.next = chunk_h.next
            while res_cur.next:
                res_cur = res_cur.next
            chunknum=0
            
        
        return res_h.next
    
    
        
        
        