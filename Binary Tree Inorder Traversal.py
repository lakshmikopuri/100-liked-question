#Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
         if root:
            left = self.inorderTraversal(root.left) if root.left else []
            val = [root.val]
            right = self.inorderTraversal(root.right) if root.right else []
            return left + val + right 
