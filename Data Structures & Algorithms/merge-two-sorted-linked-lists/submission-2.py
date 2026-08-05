# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = list1
        r = list2
        dummy = ListNode()
        d = dummy
        while l and r:
            if l.val < r.val:
                d.next = l
                l = l.next
                d = d.next
            else:
                d.next = r
                r = r.next
                d = d.next
        if l:
            d.next = l
        elif r:
            d.next = r
        return dummy.next


'''
Algorithm

dummmy node to represent head of new list
l1 head of list1
r1 head of list 2

while l1 is not null or l2 is not null:
    if l1.val < l2.val:
        dummy.next  = l1
        l1 = l1.next
    else:
        dummy.next = l2
        l2 = l2.next
#what is left
#if l2 is left then add it to the dummy.next
or if l1 is left then add it to dummy.next
if l2:
    dummy.next = l2
else:
    dummy.next = l1

    

'''