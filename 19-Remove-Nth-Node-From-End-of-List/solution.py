# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#class Solution:
#    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#        listLength = 0
#        currentNode = head
#        while currentNode != None:
#            currentNode = currentNode.next
#            listLength += 1   
#
#        if listLength == 1:
#            return None
#
#        target = listLength - (n - 1)
#        if target == 1:
#            return head.next

#        currentNode = head
#        prevNode = None
#        counter = 1

#        while counter < target:
#            currentNode = currentNode.next
#            if counter != 1:
#                prevNode = prevNode.next
#            else:
#                prevNode = head
#            counter += 1

#        if currentNode.next != None:
#            prevNode.next = currentNode.next
#        else:
#            prevNode.next = None

#        return head

# This is the chatgpt solution, but I learned a lot just looking at it
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)   # point to head so we can delete head easily
        fast = dummy
        slow = dummy

        # move fast n+1 steps ahead so the gap is exactly n
        for _ in range(n + 1):
            fast = fast.next

        # move both until fast hits the end
        while fast:
            fast = fast.next
            slow = slow.next

        # slow is now right before the node to delete
        slow.next = slow.next.next

        return dummy.next