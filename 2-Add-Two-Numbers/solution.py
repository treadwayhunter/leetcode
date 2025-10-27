class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 2->4->3   = 342
        # 5->6->4   = 465
        #           = 807
        # edge cases for numbers greater than 10 or 20
        # edge cases for one list longer than the other
        added_list = ListNode()
        current_node = added_list
        while l1 or l2:
            val = current_node.val
            if l1 and l2:
                val += l1.val + l2.val
            if l1 and not l2:
                val += l1.val
            if l2 and not l1:
                val += l2.val

            if val < 10:
                current_node.val = val
                #current_node.next = ListNode()
            elif val >= 10 < 20:
                val = val - 10
                current_node.val = val
                current_node.next = ListNode(1)
            elif val >= 20:
                val = val - 20
                current_node.val = val
                current_node.next = ListNode(2)
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if l1 or l2:
                if not current_node.next:
                    current_node.next = ListNode()
                current_node = current_node.next
                
        return added_list