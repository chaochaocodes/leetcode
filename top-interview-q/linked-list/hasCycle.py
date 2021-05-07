'''
https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the 'next' pointer. Internally, 'pos' is used to denote the index of the node that tail's 'next' pointer is connected to. *Note that pos is not passed as a parameter.

Return 'true' if there is a cycle in the linked list. Otherwise, return false. 
'''
'''
# Approach 1: Hash Table
To detect if a list is cyclic, we can check whether a node had been visited before using a hash table.  If the current node is null, we have reached the end, and there is no cycle. If current node’s reference is in the hash table, then return true.

Time: O(n). Traverse every node in the LL.  Adding a node to the hash table only costs O(1) time
Space: O(n).  Store every node in the LL in set()
'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False

'''
# Approach 2: Floyd's Cycle Finding Algorithm 
2-Pointers at different speeds -- slow pointer moves 1 step, faster pointer moves 2 steps at a time.

If there is no cycle in the list, the fast pointer will eventually reach the end and we can return false in this case.

In a cyclic list, the faster pointer will eventually lap the slow pointer.  

Time: O(n)
- No cycle: run time depends on list's length
- Has cycle: (dist bw 2 pointers) / (diff of speed) loops for faster pointer to catch up with slow pointer.  The dist is at most 'cyclic length K' and diff of speed is 1, so worst case time complexity is O(n+k), which is O(n)
Space: O(1), only use 2 nodes (slow and fast)
'''

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


# Approach 3:  Python way
class Solution:
	def hasCycle(self, head: ListNode) -> bool:
        # while slow and faster pointer: 
		while head and head.next:
			if str(head.val) == "T":
				return True
			head.val = "T"
			head = head.next
		return False