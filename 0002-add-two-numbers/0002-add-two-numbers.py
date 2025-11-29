# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #reversing the input and returning integer value
        def read(node):
            s = ""
            while node:
                s = str(node.val) + s
                node = node.next
            return (int(s))

        total = read(l1) + read(l2) 
        
        dummy = ListNode()
        curr = dummy
        for digit in reversed(str(total)):
            curr.next = ListNode(int(digit))
            curr = curr.next
            
        return dummy.next