class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr=head
        prev=None
        while curr:
            # initialize next, then prev
            next=curr.next
            curr.next=prev
            # update prev element to curr
            prev=curr
            # update curr as next (current.next)
            curr=next
        # when curr = None and next = None, left with prev
        return prev