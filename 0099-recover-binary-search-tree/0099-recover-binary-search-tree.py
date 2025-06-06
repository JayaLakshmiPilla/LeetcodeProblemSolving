class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        inorder_nodes = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            inorder_nodes.append(node)
            inorder(node.right)

        inorder(root)

        x = y = None
        for i in range(len(inorder_nodes) - 1):
            if inorder_nodes[i].val > inorder_nodes[i+1].val:
                y = inorder_nodes[i+1]
                if not x:
                    x = inorder_nodes[i]
                else:
                    break

        # Swap values of the two nodes to fix the tree
        x.val, y.val = y.val, x.val
