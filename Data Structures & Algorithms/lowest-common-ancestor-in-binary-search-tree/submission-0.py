# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # we just need to find out 
        #   1. are p and q both on either sides -> return root
        #   2. are p and q both on the same side return whatever comes first in preorder search
        if p.val<root.val<q.val:
            return root
        def dfs(node,p,q):
            if not node:
                return
            if node.val == p.val:
                return p
            if node.val == q.val:
                return q
            if p.val<node.val<q.val or q.val<node.val<p.val:
                return node
            return dfs(node.left,p,q) or dfs(node.right,p,q)
        return dfs(root,p,q)