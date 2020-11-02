# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Float[]}

# depth first search: going as deep as you can
# breadth first search: travel down one level at a time
# binary tree: at most 2 children
# queue: first in, first out (waiting in line)
# input: [3, 9, 20, null, null, 15, 7]
# output: [3, 14.5, 11]
# constraints? 
# edge cases?
# Data Structure: array/hash

# array to keep the items in each level, use 2 queues
# push item at level 1 into queue
# 1 queue for level, 1 queue for items 
# while queue is not empty, ... 

def average_of_levels(root)
    queue = []
    values_at_level = {}
    
    maxDepth = 0
    queue.push([root, 0])
    
    #BFS to make the hash
    while !queue.empty?
        current = queue.shift
        currentNode = current[0]
        currentLevel = current[1]
        # do work
        
        # checks if key already exists for level, if not, creates it
        if values_at_level[currentLevel]
            values_at_level[currentLevel] << currentNode.val
        else 
            values_at_level[currentLevel] = [currentNode.val]
        end 
        
         maxDepth = [currentLevel, maxDepth].max
        
        if currentNode.left
            queue << [currentNode.left, currentLevel + 1]
        end
        
        if currentNode.right
            queue << [currentNode.right, currentLevel + 1]
        end
    end
    
    result = []
    # average each level from values_at_level hash
    for i in 0..maxDepth do
        levelResult = values_at_level[i].sum / values_at_level[i].length.to_f
        result << levelResult
    end
    
    return result
end 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    