#Add Two Numbers
#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itse# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
         dummy = ListNode()
         temp = dummy
         carry = 0
         while (l1 != None or l2 != None) or carry:
             sum = 0
             if l1 != None:
                 sum += l1.val
                 l1 = l1.next
             if l2 != None:
                 sum += l2.val
                 l2 = l2.next
             sum += carry
             carry = sum // 10
             node = ListNode(sum % 10)
             temp.next = node
             temp = temp.next
         return dummy.next
    
