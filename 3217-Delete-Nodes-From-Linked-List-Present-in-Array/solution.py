# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numsSet = set(nums)
        
        dummy = ListNode(next=head) # having this set to 0 means it'll never be removed
        current = dummy.next
        prev = dummy

        while current: # current is not null
            if current.val in numsSet:
                prev.next = prev.next.next
            else:
                prev = prev.next
            current = current.next
        
        return dummy.next
