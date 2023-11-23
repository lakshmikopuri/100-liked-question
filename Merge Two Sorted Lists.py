#Merge Two Sorted Lists
#You are given the heads of two sorted linked lists list1 and list2.Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.Return the head of the merged linked list.
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        # If one of the lists is not fully processed, append the remaining nodes
        if l1 is not None:
            curr.next = l1
        elif l2 is not None:
            curr.next = l2
        
        return dummy.next

        
