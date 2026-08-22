# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(root, subRoot):
            if not root and subRoot:
                return False
            elif not subRoot and root:
                return False
            elif not subRoot and not root:
                return True
            elif root.val != subRoot.val:
                return False
            return (isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right))
        if root is None:
            return False
        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
            