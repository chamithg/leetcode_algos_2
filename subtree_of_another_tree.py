# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def treverse(root):
            if not root:
                return
            treverse(root.left)
            treverse(root.right)
        
        def issubTree(s,t):
            if not s and t:
                return True
            elif s and t and s.val == t.val:
                return issubTree(s.left,t.left) and issubTree(t.right,s.right)
            else:
                return False