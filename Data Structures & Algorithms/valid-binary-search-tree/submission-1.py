# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        upper,lower = float('inf'),float('-inf')
        queue = deque([(root,lower,upper)])  
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr,l,u = queue.popleft()
                if not (l<curr.val<u):
                    return False
                if curr.left:
                    queue.append((curr.left,l,curr.val))
                if curr.right:
                    queue.append((curr.right,curr.val,u))
        return True