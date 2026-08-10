# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head

        # Find the middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse second half
        prev = slow.next
        slow.next = None
        new_head = None

        while prev:
            temp = prev.next
            prev.next = new_head
            new_head = prev
            prev = temp

        # Merge the two halves
        l = head
        r = new_head

        while r:
            l_temp = l.next
            r_temp = r.next

            l.next = r
            r.next = l_temp

            l = l_temp
            r = r_temp
        
'''
Half the linked list


Reverse the right half

and match left ppointerr with right pointer

'''