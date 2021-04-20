# 1A. Iterative approach
# Complexity analysis
# Time complexity : O(n)O(n). 
# Assume that nn is the list's length, the time complexity is O(n)O(n).
# Space complexity : O(1)O(1).
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr=head
        prev=None
        while curr:
            # initalize temporary pointer variable 'next' to store curr.next value
            next=curr.next 
            # REVERSE! 
            curr.next=prev
            # update prev and curr elements
            prev=curr   # used in the next iteration
            curr=next   # move down the ll 
        # when curr = None and next = None, left with prev
        return prev

# 1B. Iterative with swap
# In python, you can swap inline elements without losing the scope or original contents of the elements.
# Don't need to set next = curr.next, initial values are preserved.
class Solution(object):        
    def reverseList(self, head):  # Iterative
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

# 2. Recursive approach
# Complexity analysis
# Time complexity : O(n)O(n). Assume that nn is the list's length, the time complexity is O(n)O(n).
# Space complexity : O(n)O(n). The extra space comes from implicit stack space due to recursion. The recursion could go up to nn levels deep.
class Solution(object):        
    def reverseList(self, head): 
        """
        :type head: ListNode
        :rtype: ListNode
        """     
        # same as: if (head == null || head.next == null) return head;
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p 

# Explanation for head.next.next = head
# Think about the origin link list : 1->2->3->4->5.
# Now assume that the last node has been reversed: 1->2->3->4<-5.
# Now you are at the node 3, you want to change 3->4 to 3<-4, 
# means let 3->next->next = 3.(3->next is 4 and 4->next = 3 is to reverse it)

# Basically, think of head as the second to last node. 
# It will make the last node's next point to the one before it. 
# head.next = None, will nullify the forward pointer (as we need to reverse). 
# Leaving this will cause a cycle from last to second last. 
# The call stack will pop returns back to the original head and do the same thing to all nodes.

