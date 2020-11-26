// diameter = length of longest path between any 2 nodes in a tree (may or may not pass through the root)

var diameterOfBinaryTree = function(root) {
  let diameter = 0

  function maxDepth(node) {
    if (!node) return 0;
    
    // assign left subtree to L, and right to R
    let L = maxDepth(node.left)
    let R = maxDepth(node.right)
    
    // update diameter  at every node level
    // if path doesn't go through the root, we get the max of them
    diameter = Math.max(diameter, L + R )
    // update largest number of edge so far, 
    // if the path goes through root, +1
    return Math.max(L, R) + 1
    }

    // return diameter of max(through root, not-through-root lengths)
    maxDepth(root)
    return diameter;
  };