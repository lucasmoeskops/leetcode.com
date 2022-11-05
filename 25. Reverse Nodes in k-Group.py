# Score:
#   Runtime: 74%
#   Memory usage: 99%

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return self.val
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        begin = ListNode(next=head)
        stack = []
        cur = head
        rev_head = begin
        while cur:
            stack.append(cur)
            cur = cur.next
            if len(stack) == k:
                while stack:
                    rev_head.next = stack.pop()
                    rev_head = rev_head.next
                rev_head.next = cur
        return begin.next
