# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = cur =  ListNode()
        
        heap = []
        for idx,i in enumerate(lists):
            if i != None:
                heapq.heappush(heap,(i.val,idx))
        while True :
            if not heap:
                break
            val,num = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            lists[num] = lists[num].next
            if lists[num] != None:
                heapq.heappush(heap,(lists[num].val,num))
        
        return res.next