# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        # id가 같은 순간을 찾아야함 (단순히 val만 같으면 안됨..)
        if not headA or not headB :
            return None
        
        curA = headA
        curB = headB
        while curA is not curB :
            
            curA = headB if curA is None else curA.next
            curB = headA if curB is None else curB.next 

        return curA
            