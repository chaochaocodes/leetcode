/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
// iteratively
var reverseList = function(head) {
  let prev = null;
  // point current node to previous node
  let curr = head;
    while (curr !== null) {
        // store prev node
        let nextTemp = curr.next
        // store next node before changing reference
        curr.next = prev
        prev = curr
        curr = nextTemp
    }
    // return new head 
    return prev;
};

// recursively
//
var reverseList = function(head) {
  if (head == null || head.next == null) return head
  let p = reverseList(head.next)
  head.next.next = head
  head.next = null
  return p
};