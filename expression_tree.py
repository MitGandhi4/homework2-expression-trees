class TreeNode:
    def __init__(self, value):
        """
        Create a node in the expression tree.
        Each node stores:
        - value (operator or operand)
        - left child
        - right child
        """
        self.value = value
        self.left = None
        self.right = None