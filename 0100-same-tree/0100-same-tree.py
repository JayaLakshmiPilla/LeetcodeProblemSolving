# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Both nodes are None, trees are identical here
        if not p and not q:
            return True
        
        # One node is None, the other is not
        if not p or not q:
            return False
        
        # Values differ
        if p.val != q.val:
            return False
        
        # Check left subtree and right subtree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
