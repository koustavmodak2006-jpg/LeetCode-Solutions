# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        def inOrder(temp):
            if temp is None:
                return

            inOrder(temp.left)
            result.append(temp.val)
            inOrder(temp.right)
        inOrder(root)

        return result