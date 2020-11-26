/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} low
 * @param {number} high
 * @return {number}
 */

// Solution #1: DFS 
// time complexity: O(n), n nodes present, visit each node exactly once in BST, at the worse case
// space complexity: O(n), space required by recursion stack when we run DFS algo.
var rangeSumBST = function(root, low, high) {
      let sum = 0
      if (root == null) return sum

      // check if value is in the given range
      if (root.val >= low && root.val <= high) {
          sum += root.val
      }
      // Approach 1: recursive DFS
      // rangeSumBST(root.left, low, high)
      // rangeSumBST(root.right, low, high)

      // Approach 2
      // at root node, if root > low, call dfs on L subtree
      if (root.val > low) {
        sum += rangeSumBST(root.left, low, high)
      }
      // at root node, if root < high, call dfs on R subtree
      if (root.val < high) {
        sum += rangeSumBST(root.right, low, high)
      }

      return sum;
  }