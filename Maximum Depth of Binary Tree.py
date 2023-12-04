# Maximum Depth of Binary Tree
#Given the root of a binary tree, return its maximum depth.A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            l = self.maxDepth(root.left)
            r = self.maxDepth(root.right)
        return 1 + max(l, r)
