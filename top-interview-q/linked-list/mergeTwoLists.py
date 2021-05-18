# Approach 1: Simple

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		if not l1 or not l2:
			return l1 if not l2 else l2

		if l1.val <= l2.val:
			pointer = head = l1
			l1 = l1.next
		else:
			pointer = head = l2
			l2 = l2.next
	   
		while l1 and l2:
			if l1.val <= l2.val:
				pointer.next = l1
				l1 = l1.next
			else:
				pointer.next = l2
				l2 = l2.next
			pointer = pointer.next
		
		pointer.next = l1 if l1 else l2
		
		return head

# Approach 2:  Recursion
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ## Base cases aka stop condition
        # both l1 and l2 are empty list
        if not l1 and not l2:
            return None
        
        # l1 is empty, directly return l2
        elif not l1:
            return l2
        
        # l2 is empty, directly return l1
        elif not l2:
            return l1
        
        ## General cases
        # Compare node value and merge
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2



# Approach 3A
# If both lists are non-empty, make sure 'a' starts smaller, use its head as result, and merge the remainders behind it. Otherwise, i.e., if one or both are empty, I just return what's there.
class Solution:
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b


# Approach 3B
# First make sure that a is the "better" one (meaning b is None or has larger/equal value). Then merge the remainders behind a.

def mergeTwoLists(self, a, b):
    if not a or b and a.val > b.val:
        a, b = b, a
    if a:
        a.next = self.mergeTwoLists(a.next, b)
    return a


