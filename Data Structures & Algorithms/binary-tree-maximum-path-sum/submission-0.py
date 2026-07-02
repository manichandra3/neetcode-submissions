# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # This will hold our absolute highest path sum found anywhere
        self.global_max = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # Recurse down the tree. 
            # KADANE'S LOGIC: If a branch is negative, we take 0 (ignore it).
            left_branch = max(dfs(node.left), 0)
            right_branch = max(dfs(node.right), 0)
            
            # The maximum path if THIS node is the highest point (the Peak)
            current_peak_sum = node.val + left_branch + right_branch
            
            # Update our global max if we found a better closed path
            self.global_max = max(self.global_max, current_peak_sum)
            
            # Return the max path that can be extended up to the parent
            return node.val + max(left_branch, right_branch)
            
        dfs(root)
        return self.global_max